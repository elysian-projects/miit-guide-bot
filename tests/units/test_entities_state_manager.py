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


def test__reset_data():
    state_manager = StateManager()

    state_manager.reset_data()

    assert state_manager.get_location() == "unknown"
    assert state_manager.is_location_chosen() == False
    assert state_manager.get_current_step() == 0
