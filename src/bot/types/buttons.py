from .external import Enumerable, unique


@unique
class Button(Enumerable):
    TO_HUB = "🏠 Вернуться в меню"
    NEXT = "➡️ Далее"
    YES = "✅ Да!"
    NO_BACK_TO_HUB = "❌ Нет, вернуться в меню"
