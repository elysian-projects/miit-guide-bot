from src.bot.utils.database import parse_response


def test__parse_response():
    assert parse_response('{"name": "username", "age": 20}') == {"name": "username", "age": 20}
    assert parse_response("{}") == {}
