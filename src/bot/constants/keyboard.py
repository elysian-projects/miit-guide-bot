from ..constants.locations import LOCATION_LABELS
from ..types.buttons import Button
from ..utils.keyboard import create_inline_keyboard, create_menu_keyboard


class Keyboard:
    MENU_YES__NO = create_menu_keyboard([Button.YES, Button.NO_BACK_TO_HUB], resize_keyboard = True, one_time_keyboard = True)
    MENU_NEXT__TO_HUB = create_menu_keyboard([Button.NEXT, Button.TO_HUB], resize_keyboard = True, one_time_keyboard = True)

    INLINE_LOCATIONS = create_inline_keyboard(LOCATION_LABELS)
