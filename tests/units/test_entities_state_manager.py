import pytest
from src.bot.entities.state_manager import StateManager


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


def test__get_data_by_field():
    state_manager = StateManager()

    assert state_manager.get_data_by_field("name") == None

    state_manager.set_points_list([{"name": "value1"}, {"name": "value2"}])
    assert state_manager.get_data_by_field("name") == "value1"

    state_manager.next_step()
    assert state_manager.get_data_by_field("name") == "value2"

    state_manager.next_step()
    assert state_manager.get_data_by_field("name") == None

    state_manager.reset_data()
    assert state_manager.get_data_by_field("name") == None


def test__set_points_list():
    state_manager = StateManager()

    assert state_manager.get_points_list() == []
    assert len(state_manager.get_points_list()) == 0

    state_manager.set_points_list(["value1", "value2"])

    assert state_manager.get_points_list() == ["value1", "value2"]
    assert len(state_manager.get_points_list()) == 2

    state_manager.reset_data()
    assert len(state_manager.get_points_list()) == 0


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

    assert state_manager.get_location() == None
    assert state_manager.is_location_chosen() == False
    assert state_manager.get_current_step() == 0
    assert state_manager.get_points_list() == []
    assert len(state_manager.get_points_list()) == 0
    assert state_manager.is_end == False
