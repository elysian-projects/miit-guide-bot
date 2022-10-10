from .external import Enumerable, unique


@unique
class Button(Enumerable):
    START = "Начать экскурсию!"
    TO_HUB = "Вернуться в меню"
    NEXT = "Далее"
    CANNOT_FIND = "Не могу найти"
    FOUND = "На месте"
    YES = "✅ Да!"
    NO_BACK_TO_HUB = "❌ Нет, вернуться в меню"
