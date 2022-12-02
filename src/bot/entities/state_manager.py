from typing import Dict, List

from ..constants.state import *
from ..entities.user_store import UserData
from ..types.location import Point
from ..utils.database import raise_no_user_found_exception
from ..utils.location import format_point_data, is_valid_location

__users: Dict[str, UserData] = {}

class StateManager:
    def __init__(self):
        pass


    def add_user(self, chat_id) -> None:
        if(not chat_id in __users):
            __users[chat_id] = UserData()


    def set_location(self, location: str, chat_id: str) -> None:
        if(not is_valid_location(location)):
            raise TypeError("Incorrect location was given!")

        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)

        __users[chat_id].location = format_point_data(location)


    def set_points_list(self, points_list: List[object], chat_id: str) -> None:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)

        __users[chat_id].points_list = [format_point_data(_point) for _point in points_list]
        __users[chat_id].max_steps = len(points_list)


    def next_step(self, chat_id: str) -> None:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)

        __users[chat_id].current_step += 1

        if(__users[chat_id].current_step == __users[chat_id].max_steps - 1):
            __users[chat_id].is_end = True


    def get_location(self, chat_id: str) -> str:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return __users[chat_id].location

    def get_current_step(self, chat_id: str) -> int:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return __users[chat_id].current_step

    def get_max_steps(self, chat_id) -> int:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return __users[chat_id].max_steps

    def get_points_list(self, chat_id) -> List[Point]:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return __users[chat_id].points_list

    def get_point_data(self, chat_id) -> Point:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)

        data = __users[chat_id].points_list
        step = __users[chat_id].current_step

        if(len(data) == 0 or step >= len(data)):
            return Point()

        return data[step]

    def get_is_end(self, chat_id) -> int:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return __users[chat_id].is_end


    def is_location_chosen(self, chat_id: str) -> bool:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return __users[chat_id].location != None


    def user_exists(self, chat_id):
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)
        return chat_id in __users


    def reset_data(self, chat_id) -> None:
        if(not self.user_exists(chat_id)):
            raise_no_user_found_exception(chat_id)

        __users[chat_id].reset()
