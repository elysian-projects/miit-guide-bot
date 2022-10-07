from typing import Any, List

from ..types.external import AIOGramTypes


def create_menu_keyboard(
    items: List[str] = [],
    resize_keyboard: bool or None = None,
    one_time_keyboard: bool or None = None,
    input_field_placeholder: Any or None = None,
    selective: bool or None = None,
) -> AIOGramTypes.ReplyKeyboardMarkup:
    """
    Создаёт клавиатуру в меню (около поля ввода)

    :param items - массив строк, которые будут отображаться в виде кнопок
    :param resize_keyboard - параметр, выставляющий, нужно ли менять размер кнопок `по вертикали`
    :param one_time_keyboard - параметр, скрывающий клавиатуру после первого нажатия на кнопку
    :param input_field_placeholder - строка, которая будет отображаться в поле ввода после появления кнопок
    :param selective - показать клавиатуру конкретным типам пользователей

    @see https://core.telegram.org/bots/api#replykeyboardmarkup
    """

    markup = AIOGramTypes.ReplyKeyboardMarkup(
        resize_keyboard = resize_keyboard,
        one_time_keyboard = one_time_keyboard,
        input_field_placeholder = input_field_placeholder,
        selective = selective,
    )

    for button_text in items:
        keyboard_button = AIOGramTypes.KeyboardButton(button_text)
        markup.add(keyboard_button)

    return markup


def create_inline_keyboard(
    items: List[str] = []
) -> AIOGramTypes.InlineKeyboardMarkup:
    """
    Создаёт клавиатуру, которая крепится к определённому сообщению

    :param items - массив строк, которые будут отображаться в виде кнопок

    @see https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    markup = AIOGramTypes.InlineKeyboardMarkup()

    for button_text in items:
        inline_button = AIOGramTypes.InlineKeyboardButton(button_text, callback_data = button_text)
        markup.add(inline_button)

    return markup
