from typing import List

from ..types.location import Location

AVAILABLE_LOCATIONS: List[str] = [Location[location] for location in Location]

LOCATION_LABELS = [_location["label"] for _location in AVAILABLE_LOCATIONS]
LOCATION_VALUES = [_location["value"] for _location in AVAILABLE_LOCATIONS]
