from src.bot.constants.locations import LOCATION_LABELS, LOCATION_VALUES
from src.bot.types.location import LocationProps
from src.bot.utils.location import (format_location_for_database,
                                    get_location_property, is_valid_location)


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

def test__get_location_property():
    assert get_location_property("street", LocationProps.label) == "Улица"
    assert get_location_property("street ", LocationProps.label) == "Улица"
    assert get_location_property("building_1", LocationProps.label) == "Корпус 1"
    assert get_location_property("building_1 ", LocationProps.label) == "Корпус 1"
    assert get_location_property("Улица", LocationProps.label) == "Улица"
    assert get_location_property(" Улица", LocationProps.label) == "Улица"
    assert get_location_property("Корпус 1", LocationProps.label) == "Корпус 1"
    assert get_location_property("Корпус 1 ", LocationProps.label) == "Корпус 1"

    assert get_location_property("stret", LocationProps.label) == None
    assert get_location_property("Корпус1", LocationProps.label) == None

    assert get_location_property("Улица", LocationProps.value) == "street"
    assert get_location_property("Улица ", LocationProps.value) == "street"
    assert get_location_property("Корпус 1", LocationProps.value) == "building_1"
    assert get_location_property(" Корпус 1", LocationProps.value) == "building_1"
    assert get_location_property("street", LocationProps.value) == "street"
    assert get_location_property("street ", LocationProps.value) == "street"
    assert get_location_property("building_1", LocationProps.value) == "building_1"
    assert get_location_property("building_1 ", LocationProps.value) == "building_1"

    assert get_location_property("stret", LocationProps.value) == None
    assert get_location_property("Корпус1", LocationProps.value) == None
