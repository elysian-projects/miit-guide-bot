from .external import Enumerable


class StateField(Enumerable):
    LOCATION = "location"
    CURRENT_STEP = "current_step"
    MAX_STEPS = "max_steps"
    POINTS_LIST = "points_list"
    IS_END = "is_end"
