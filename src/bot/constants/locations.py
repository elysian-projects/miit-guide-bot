from typing import List

from ..types.location import Location

AVAILABLE_LOCATIONS: List[str] = [Location[location]["label"] for location in Location if location != "unknown"]
