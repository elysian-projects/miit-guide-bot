def get_nested_path(field: str, divider: str = ".") -> list[list]:
    """ Переводит строку в массив массивов таким образом: "Telegram.TOKEN.FIRST" -> ["Telegram"]["TOKEN"]["FIRST"] """
    return __nest_fields(__convert_path_to_array(field, divider))

def __convert_path_to_array(path: str, divider: str) -> list[str]:
    return path.split(divider)

def __nest_fields(paths: list[str]) -> list[list[any]] | list[str]:
    return "rest"
