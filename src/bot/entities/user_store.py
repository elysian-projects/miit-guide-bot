from typing import List

from ..constants.state import *
from ..types.location import Point


class UserData:
    location: str
    current_step: int
    max_steps: int
    points_list: List[Point]
    is_end: bool


    def __init__(self):
      self.reset()


    def reset(self):
        self.location = DEFAULT_LOCATION
        self.current_step = DEFAULT_CURRENT_STEP
        self.max_steps = DEFAULT_MAX_STEPS
        self.points_list = DEFAULT_POINTS_LIST
        self.is_end = DEFAULT_IS_END
