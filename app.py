import os
import json
import urllib
import boto3
from chalice import Chalice, Response
from chalicelib.modules.helpers import logger, EXCHANGE_RATES_FILE_NAME
from chalicelib.modules.telegram import sendMessage, answerInlineQuery

app = Chalice(app_name="unitconversionbot")
app.debug = os.environ.get("DEBUG", not os.environ.get("AWS_REGION"))


@app.route("/")
def index():
    return Response(
        status_code=301,
        body="",
        headers={"Location": "https://telegram.me/UnitConversionBot"},
    )


@app.route("/webhook", methods=["POST"])
def telegram_webhook():
    request = app.current_request
    body = request.json_body or {}
    logger.debug(body)

    if "message" in body:
        response = sendMessage(body)
    elif "inline_query" in body:
        response = answerInlineQuery(body)
    else:
        response = {}

    logger.debug(response)
    return response


s3 = boto3.client("s3")


@app.schedule("rate(2 hours)")
def update_exchange_rates(event):
    try:
        OPENEXHANGERATES_API_KEY = os.environ["OPENEXHANGERATES_API_KEY"]
        S3_BUCKET = os.environ["S3_BUCKET"]
        apiUrl = (
            "https://openexchangerates.org/api/latest.json?show_alternative=1&app_id="
            + OPENEXHANGERATES_API_KEY
        )
        response = urllib.request.urlopen(apiUrl)
        content = response.read()
        rates = json.loads(content)
        if "rates" not in rates:
            raise Exception(rates)
        s3.put_object(
            ACL="public-read",
            ContentType="application/json",
            Bucket=S3_BUCKET,
            Key=EXCHANGE_RATES_FILE_NAME,
            Body=json.dumps(rates),
        )
        MONITOR_PING_URL = os.environ["MONITOR_PING_URL"]
        if MONITOR_PING_URL:
            urllib.request.urlopen(MONITOR_PING_URL, timeout=10)
        return
        # See https://github.com/aws/chalice/issues/242#issuecomment-397945077
        s3.put_object_acl(
            ACL="public-read", Bucket=S3_BUCKET, Key=EXCHANGE_RATES_FILE_NAME
        )
    except Exception as error:
        logger.error(error)
