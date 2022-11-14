import pytest

from src.bot.constants.state import *
from src.bot.entities.state_manager import StateManager
from src.bot.utils.location import format_point_data

_default_points_list = [
    {"name": "name1", "description": "description1", "picture": "picture1", "links": ["link1", "link2"]},
    {"name": "name2", "description": "description2", "picture": "picture2", "links": ["link1", "link2"]}
]


def test__set_location():
    state_manager = StateManager()

    assert state_manager.is_location_chosen() == False

    state_manager.set_location("street")

    assert state_manager.get_location() == "street"
    assert state_manager.is_location_chosen() == True

    state_manager.set_location("Улица")

    assert state_manager.get_location() == "street"
    assert state_manager.is_location_chosen() == True

    state_manager.set_location("building_1")

    assert state_manager.get_location() == "building_1"
    assert state_manager.is_location_chosen() == True

    state_manager.set_location("Корпус 1")

    assert state_manager.get_location() == "building_1"
    assert state_manager.is_location_chosen() == True

    # Выкидывает исключение, если переданная локация не является корректной
    with pytest.raises(TypeError):
        state_manager.set_location("location1")


def test__set_points_list():
    state_manager = StateManager()

    assert state_manager.get_points_list() == []

    state_manager.set_points_list(_default_points_list)

    assert state_manager.get_points_list() == [format_point_data(_point) for _point in _default_points_list]

    state_manager.reset_data()
    assert state_manager.get_points_list() == []


def test__get():
    state_manager = StateManager()

    assert state_manager.get_location() == DEFAULT_LOCATION
    assert state_manager.get_current_step() == DEFAULT_CURRENT_STEP
    assert state_manager.get_max_steps() == DEFAULT_MAX_STEPS
    assert state_manager.get_points_list() == DEFAULT_POINTS_LIST
    assert state_manager.is_end == DEFAULT_IS_END

    state_manager.set_location("street")
    state_manager.set_points_list(_default_points_list)

    assert state_manager.get_location() == "street"
    assert state_manager.get_current_step() == 0
    assert state_manager.get_max_steps() == 2
    assert state_manager.is_end == False

    sample_list = [format_point_data(_point) for _point in _default_points_list]
    state_list = state_manager.get_points_list()

    for index in range(len(state_list)):
        assert state_list[index] == sample_list[index]

    state_manager.next_step()

    assert state_manager.is_end == True


def test__get_current_step_data():
    state_manager = StateManager()

    current_data = state_manager.get_point_data()

    assert current_data.name == None

    state_manager.set_points_list(_default_points_list)
    current_data = state_manager.get_point_data()

    assert current_data.name == "name1"

    state_manager.next_step()
    current_data = state_manager.get_point_data()

    assert current_data.name == "name2"

    state_manager.next_step()
    current_data = state_manager.get_point_data()

    assert current_data.name == None

    state_manager.reset_data()
    current_data = state_manager.get_point_data()

    assert current_data.name == None


def test__next_step():
    state_manager = StateManager()

    assert state_manager.get_current_step() == 0

    state_manager.next_step()
    assert state_manager.get_current_step() == 1

    state_manager.next_step()
    assert state_manager.get_current_step() == 2

    state_manager.next_step()
    state_manager.next_step()
    assert state_manager.get_current_step() == 4


def test__is_end():
    state_manager = StateManager()

    state_manager.set_location("street")
    state_manager.set_points_list(["point1", "point2"])

    assert state_manager.is_end == False

    state_manager.next_step()
    assert state_manager.get_current_step() == 1
    assert state_manager.is_end == True


def test__is_location_chosen():
    state_manager = StateManager()

    assert state_manager.is_location_chosen() == False

    state_manager.set_location("street")
    assert state_manager.is_location_chosen() == True


def test__reset_data():
    state_manager = StateManager()

    state_manager.set_location("street")
    state_manager.set_points_list(["value1", "value2"])
    state_manager.next_step()

    state_manager.reset_data()

    assert state_manager.get_location() == DEFAULT_LOCATION
    assert state_manager.get_current_step() == DEFAULT_CURRENT_STEP
    assert state_manager.get_points_list() == DEFAULT_POINTS_LIST
    assert state_manager.is_end == DEFAULT_IS_END
    assert state_manager.is_location_chosen() == False
