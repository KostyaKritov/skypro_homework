from typing import Dict, List, Union


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список операций по заданному состоянию.
    Параметры:
    - data (List[Dict]): Список словарей с данными операций.
    - state (str): Статус для фильтрации. По умолчанию 'EXECUTED'.
    Возвращает:
    List[Dict]: Список операций с заданным статусом.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, Union[str, int]]], descending: bool = True) -> List[Dict[str, Union[str, int]]]:
    """
    Сортирует список словарей по ключу 'date' в порядке убывания по умолчанию.
    :param data: Список словарей, содержащих информацию об операциях
    :param descending: Логическое значение, определяющее порядок сортировки
    :return: Новый отсортированный список словарей
    """
    return sorted(data, key=lambda x: x['date'], reverse=descending)
