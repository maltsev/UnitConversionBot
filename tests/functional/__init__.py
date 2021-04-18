import sys
import random
import json
import hashlib
from chalice.test import Client
from app import app


def make_request(body):
    with Client(app) as client:
        response = client.http.post(
            '/webhook',
            headers={
                'Content-Type': 'application/json',
            },
            body=json.dumps(body),
        )
        return response.json_body


def get_body(is_inline=False, **kwargs):
    body = {
        'update_id': random.randint(1, sys.maxsize),
    }
    if is_inline:
        body['inline_query'] = {
            'id': random.randint(1, sys.maxsize),
            **kwargs,
        }
    else:
        body['message'] = {
            'chat': {
                'id': random.randint(1, sys.maxsize),
            },
            **kwargs,
        }

    return body


def get_request(request_body, text, parse_mode=None):
    request = {
        'chat_id': request_body['message']['chat']['id'],
        'disable_notification': True,
        'disable_web_page_preview': True,
        'method': 'sendMessage',
        'text': text,
    }
    if parse_mode:
        request['parse_mode'] = parse_mode

    return request


def get_inline_request(request_body, title, message_text, description):
    result = {
        'id': hashlib.md5(title.encode('utf-8')).hexdigest(),
        'message_text': message_text,
        'title': title,
        'type': 'article',
    }

    if description:
        result['description'] = description

    return {
        'cache_time': 43200,
        'inline_query_id': request_body['inline_query']['id'],
        'is_personal': False,
        'method': 'answerInlineQuery',
        'results': [result],
    }


def check(expected_text, **kwargs):
    parse_mode = kwargs.pop('parse_mode', None)
    request_body = get_body(**kwargs)
    real_json_body = make_request(request_body)
    expected_json_body = get_request(request_body, expected_text, parse_mode=parse_mode)
    assert real_json_body == expected_json_body, real_json_body


def check_inline(expected_title, expected_text, **kwargs):
    request_body = get_body(is_inline=True, **kwargs)
    real_json_body = make_request(request_body)
    expected_json_body = get_inline_request(request_body, expected_title, expected_text, kwargs.get('description', ''))
    real_json_body['results'] = json.loads(real_json_body['results'])
    assert real_json_body == expected_json_body, real_json_body
