from typing import Dict, List, Union

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстура с тестовыми данными
@pytest.fixture
def sample_data() -> List[Dict[str, Union[str, int]]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("UNKNOWN", 0),
])
def test_filter_by_state(sample_data: List[Dict[str, Union[str, int]]], state: str, expected_count: int) -> None:
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count


# Тесты для sort_by_date
def test_sort_by_date_descending(sample_data: List[Dict[str, Union[str, int]]]) -> None:
    sorted_data = sort_by_date(sample_data)
    assert isinstance(sorted_data[0]['date'], str)  # Уточняем тип для mypy
    assert isinstance(sorted_data[-1]['date'], str)  # Уточняем тип для mypy
    assert sorted_data[0]['date'] > sorted_data[-1]['date']


def test_sort_by_date_ascending(sample_data: List[Dict[str, Union[str, int]]]) -> None:
    sorted_data = sort_by_date(sample_data, descending=False)
    assert isinstance(sorted_data[0]['date'], str)  # Уточняем тип для mypy
    assert isinstance(sorted_data[-1]['date'], str)  # Уточняем тип для mypy
    assert sorted_data[0]['date'] < sorted_data[-1]['date']
