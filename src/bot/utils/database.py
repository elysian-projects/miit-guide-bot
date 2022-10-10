import json


def parse_response(response: str):
    return json.loads(response)
