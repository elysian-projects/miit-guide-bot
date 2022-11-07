from aiogram import types as AIOGramTypes
from src.bot.utils.keyboard import (create_inline_keyboard,
                                    create_menu_keyboard, remove_keyboard)


def test__create_inline_keyboard():
    assert create_inline_keyboard(["Button 1"]) == AIOGramTypes.InlineKeyboardMarkup()\
        .add(AIOGramTypes.InlineKeyboardButton("Button 1", callback_data = "Button 1"))

    assert create_inline_keyboard(["Button 1", "Button 2"]) == AIOGramTypes.InlineKeyboardMarkup()\
        .add(AIOGramTypes.InlineKeyboardButton("Button 1", callback_data = "Button 1"))\
        .add(AIOGramTypes.InlineKeyboardButton("Button 2", callback_data = "Button 2"))

    assert create_inline_keyboard([]) == AIOGramTypes.InlineKeyboardMarkup()


def test__create_menu_keyboard():
    assert create_menu_keyboard(["Button 1"]) == AIOGramTypes.ReplyKeyboardMarkup()\
        .add(AIOGramTypes.KeyboardButton("Button 1"))

    assert create_menu_keyboard(["Button 1", "Button 2"]) == AIOGramTypes.ReplyKeyboardMarkup()\
        .add(AIOGramTypes.KeyboardButton("Button 1"))\
        .add(AIOGramTypes.KeyboardButton("Button 2"))

    assert create_menu_keyboard([]) == AIOGramTypes.ReplyKeyboardMarkup()


def test__remove_keyboard():
    assert remove_keyboard() == AIOGramTypes.ReplyKeyboardRemove()
