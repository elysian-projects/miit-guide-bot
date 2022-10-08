from typing import List

from ..types.location import Location

AVAILABLE_LOCATIONS: List[str] = [str(location) for location in Location if location != Location.UNKNOWN]
