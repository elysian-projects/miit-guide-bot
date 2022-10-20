from typing import List

Location = {
    "street": {
        "label": "Улица",
        "value": "street"
    },
    "building_1": {
        "label": "Корпус 1",
        "value": "building_1"
    }
}


AVAILABLE_LOCATIONS: List[str] = [Location[location] for location in Location]

LOCATION_LABELS = [_location["label"] for _location in AVAILABLE_LOCATIONS]
LOCATION_VALUES = [_location["value"] for _location in AVAILABLE_LOCATIONS]
