from project.src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от входных данных.
    Параметры:
    account_info (str): строка, содержащая тип и номер карты или счета.
    Возвращает:
    str: строка с замаскированным номером.
    """
    parts = account_info.rsplit(" ", 1)
    if len(parts) != 2:
        raise ValueError("Неверный формат данных. Ожидается строка с типом и номером.")

    account_type, number_str = parts[0], parts[1]

    try:
        number = int(number_str)
    except ValueError:
        raise ValueError("Номер должен содержать только цифры.")

    # Маскировка номера в зависимости от типа
    if account_type.lower().startswith(("visa", "mastercard", "maestro")):
        masked_number = get_mask_card_number(number)
    elif account_type.lower().startswith("счет"):
        masked_number = get_mask_account(number)
    else:
        raise ValueError("Неверный тип счета или карты.")

    return f"{account_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".
    Параметры:
    date_str (str): дата в формате "ГГГГ-ММ-ДДTчч:мм:сс".
    Возвращает:
    str: дата в формате "ДД.ММ.ГГГГ".
    """
    try:
        date = date_str.split("T")[0]
        year, month, day = date.split("-")
        return f"{day}.{month}.{year}"
    except ValueError:
        raise ValueError("Неверный формат даты.")
