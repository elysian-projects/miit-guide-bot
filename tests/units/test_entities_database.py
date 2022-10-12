from src.bot.entities.database import Database


def test__get_location():
    database = Database()

    data = database.get_data_from_location("street")

    assert type(data) == list
    assert len(data) != 0

    data = database.get_data_from_location("building_1")

    assert type(data) == list
    assert len(data) != 0

    data = database.get_data_from_location("building1")

    assert type(data) == list
    assert len(data) == 0
