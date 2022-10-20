from src.bot.types.external import Enumerable


def test__enumerable():
    class Color(Enumerable):
        RED = "red"
        BLUE = "blue"
        GREEN = "green"

    assert Color.RED == "red"
    assert Color.BLUE == "blue"
    assert Color.GREEN == "green"

    assert type(Color.RED) == str
    assert type(Color.BLUE) == str
    assert type(Color.GREEN) == str

    assert type(str(Color.RED)) == str
    assert type(str(Color.BLUE)) == str
    assert type(str(Color.GREEN)) == str
