import json


def parse_response(response: str):
    return json.loads(response)


def raise_no_user_found_exception(chat_id: str):
    raise IndexError(f"No user with id {chat_id} found!")