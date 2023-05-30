def get_val(data: dict, key, default="None"):
    """
    Извлекает из словаря значение по его ключу, если он существует.
    Если ключа не существует, возвращает значение по умолчанию.
    :param data: dict
    :param key: ключ словаря
    :param default: значение по умолчанию
    :return: value по ключу словаря
    """
    if key not in data.keys():
        return default
    else:
        return data[key]
