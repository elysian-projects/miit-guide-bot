from src.bot.constants.locations import LOCATION_LABELS, LOCATION_VALUES
from src.bot.utils.location import (format_location_for_database,
                                    is_valid_location)


def test__is_valid_location():
    assert is_valid_location("street") == True
    assert is_valid_location("street ") == True
    assert is_valid_location("Улица") == True
    assert is_valid_location("building_1") == True
    assert is_valid_location("Корпус 1") == True
    assert is_valid_location(LOCATION_VALUES[0]) == True
    assert is_valid_location(LOCATION_LABELS[0]) == True

    assert is_valid_location("building1") == False
    assert is_valid_location("stret") == False
    assert is_valid_location("") == False

def test__format_location_for_database():
    assert format_location_for_database("street") == "street"
    assert format_location_for_database("street ") == "street"
    assert format_location_for_database("Улица") == "street"
    assert format_location_for_database("Улица ") == "street"
    assert format_location_for_database("building_1") == "building_1"
    assert format_location_for_database("building_1 ") == "building_1"
    assert format_location_for_database("Корпус 1") == "building_1"
    assert format_location_for_database("Корпус 1 ") == "building_1"

    assert format_location_for_database("building1") == None
    assert format_location_for_database("stret") == None
