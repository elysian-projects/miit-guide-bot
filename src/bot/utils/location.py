from ..constants.locations import AVAILABLE_LOCATIONS


def is_valid_location(location: str) -> bool:
    return location in AVAILABLE_LOCATIONS

def format_location_for_database(location: str) -> str | None:
    _locations = {
        "Улица": "street",
        "Корпус 1": "building_1"
    }

    try:
        return _locations[location]
    except KeyError as e:
        print(repr(e))
        return None
