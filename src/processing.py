from typing import Dict, List


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


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.
    Параметры:
    - data (List[Dict]): Список словарей с данными операций.
    - descending (bool): Порядок сортировки. True для убывания, False для возрастания.
    Возвращает:
    List[Dict]: Отсортированный по дате список операций.
    """
    return sorted(data, key=lambda x: x.get('date'), reverse=descending)
