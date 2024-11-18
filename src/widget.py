import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(text: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа входных данных.
    """
    # Определяем, что это карта или счет
    if "Счет" in text:
        # Извлекаем номер счета и маскируем его
        account_number = re.search(r"\d{8,}", text)
        if account_number:
            masked_number = get_mask_account(int(account_number.group(0)))
            return text.replace(account_number.group(0), masked_number)
    else:
        # Извлекаем номер карты и маскируем его
        card_number = re.search(r"\d{16}", text)
        if card_number:
            masked_number = get_mask_card_number(int(card_number.group(0)))
            return text.replace(card_number.group(0), masked_number)
    return text


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
