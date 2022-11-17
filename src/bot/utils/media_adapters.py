from aiogram import types as AIOGramTypes


def create_array_photo(media) -> list:
    media_group = []

    for photo in media:
        if photo:
            is_url = "https://" in photo or "http://" in photo
            media_group.append(AIOGramTypes.InputMediaPhoto(photo if is_url else open(photo, 'rb')))

    return media_group
