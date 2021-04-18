from tests.functional import get_body, make_request, check


def test_commandNotFound():
    check(
        "Sorry, I don't understand your command.",
        text='/someCommand 1 m² to ft',
        parse_mode=None,
    )


def test_noMessageText():
    request_body = get_body()
    real_json_body = make_request(request_body)
    assert real_json_body == {}


def test_noChatId(caplog):
    request_body = get_body(text='/someCommand 1 m² to ft')
    del request_body['message']['chat']['id']
    real_json_body = make_request(request_body)
    assert real_json_body == {'error': 'Chat ID is empty'}
    assert 'Chat ID is empty' in caplog.text
