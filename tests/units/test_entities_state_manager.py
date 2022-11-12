import pytest

from src.bot.constants.state import *
from src.bot.entities.state_manager import StateField, StateManager


def test__set_location():
    state_manager = StateManager()

    assert state_manager.is_location_chosen() == False

    state_manager.set_location("street")

    assert state_manager.get(StateField.LOCATION) == "street"
    assert state_manager.is_location_chosen() == True

    state_manager.set_location("Улица")

    assert state_manager.get(StateField.LOCATION) == "street"
    assert state_manager.is_location_chosen() == True

    state_manager.set_location("building_1")

    assert state_manager.get(StateField.LOCATION) == "building_1"
    assert state_manager.is_location_chosen() == True

    state_manager.set_location("Корпус 1")

    assert state_manager.get(StateField.LOCATION) == "building_1"
    assert state_manager.is_location_chosen() == True

    # Выкидывает исключение, если переданная локация не является корректной
    with pytest.raises(TypeError):
        state_manager.set_location("location1")


def test__get():
    state_manager = StateManager()

    assert state_manager.get(StateField.LOCATION) == DEFAULT_LOCATION
    assert state_manager.get(StateField.CURRENT_STEP) == DEFAULT_CURRENT_STEP
    assert state_manager.get(StateField.MAX_STEPS) == DEFAULT_MAX_STEPS
    assert state_manager.get(StateField.POINTS_LIST) == DEFAULT_POINTS_LIST
    assert state_manager.get(StateField.IS_END) == DEFAULT_IS_END

    # Запрос несуществующего поля
    assert state_manager.get("invalid") == None

    points_list = ["value1", "value2"]

    state_manager.set_location("street")
    state_manager.set_points_list(points_list)

    assert state_manager.get(StateField.LOCATION) == "street"
    assert state_manager.get(StateField.CURRENT_STEP) == 0
    assert state_manager.get(StateField.MAX_STEPS) == 2
    assert state_manager.get(StateField.POINTS_LIST) == points_list
    assert state_manager.get(StateField.IS_END) == False

    state_manager.next_step()

    assert state_manager.get(StateField.IS_END) == True


def test__get_current_step_data():
    state_manager = StateManager()

    assert state_manager.get_current_step_data("name") == None

    state_manager.set_points_list([{"name": "value1"}, {"name": "value2"}])
    assert state_manager.get_current_step_data("name") == "value1"
    assert state_manager.get_current_step_data("invalid") == None

    state_manager.next_step()
    assert state_manager.get_current_step_data("name") == "value2"

    state_manager.next_step()
    assert state_manager.get_current_step_data("name") == None

    state_manager.reset_data()
    assert state_manager.get_current_step_data("name") == None


def test__set_points_list():
    state_manager = StateManager()

    assert state_manager.get(StateField.POINTS_LIST) == []

    state_manager.set_points_list(["value1", "value2"])

    assert state_manager.get(StateField.POINTS_LIST) == ["value1", "value2"]

    state_manager.reset_data()
    assert state_manager.get(StateField.POINTS_LIST) == []


def test__next_step():
    state_manager = StateManager()

    assert state_manager.get(StateField.CURRENT_STEP) == 0

    state_manager.next_step()
    assert state_manager.get(StateField.CURRENT_STEP) == 1

    state_manager.next_step()
    assert state_manager.get(StateField.CURRENT_STEP) == 2

    state_manager.next_step()
    state_manager.next_step()
    assert state_manager.get(StateField.CURRENT_STEP) == 4


def test__is_end():
    state_manager = StateManager()

    state_manager.set_location("street")
    state_manager.set_points_list(["point1", "point2"])

    assert state_manager.is_end == False

    state_manager.next_step()
    assert state_manager.get(StateField.CURRENT_STEP) == 1
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

    assert state_manager.get(StateField.LOCATION) == DEFAULT_LOCATION
    assert state_manager.get(StateField.CURRENT_STEP) == DEFAULT_CURRENT_STEP
    assert state_manager.get(StateField.POINTS_LIST) == DEFAULT_POINTS_LIST
    assert state_manager.get(StateField.IS_END) == DEFAULT_IS_END
    assert state_manager.is_location_chosen() == False
