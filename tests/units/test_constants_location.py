from src.bot.constants.locations import LOCATION_LABELS, LOCATION_VALUES


def test__location_labels():
    assert "Улица" in LOCATION_LABELS
    assert "Корпус 1" in LOCATION_LABELS

    assert "unknown" not in LOCATION_LABELS

def test__location_values():
    assert "street" in LOCATION_VALUES
    assert "building_1" in LOCATION_VALUES

    assert "unknown" not in LOCATION_VALUES
