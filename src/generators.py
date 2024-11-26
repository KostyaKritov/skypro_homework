from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте.
    :param transactions: Список словарей с транзакциями.
    :param currency: Код валюты для фильтрации.
    :return: Итератор с транзакциями, где валюта совпадает с заданной.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Возвращает описания транзакций по очереди.
    :param transactions: Список словарей с транзакциями.
    :return: Итератор строк, содержащих описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в диапазоне от start до stop в формате XXXX XXXX XXXX XXXX.
    :param start: Начальное значение диапазона (включительно).
    :param stop: Конечное значение диапазона (включительно).
    :return: Итератор строк в формате номера карты.
    """
    for number in range(start, stop + 1):
        formatted_number = f"{number:016}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
