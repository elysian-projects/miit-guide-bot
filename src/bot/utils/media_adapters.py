from aiogram import types as AIOGramTypes
from typing import List


def create_array_photo(media: List[str]) -> List:
    media_group = []

    for photo in media:
        if photo:
            is_url = "https://" in photo or "http://" in photo
            media_group.append(AIOGramTypes.InputMediaPhoto(photo if is_url else open(photo, 'rb')))

    return media_group
