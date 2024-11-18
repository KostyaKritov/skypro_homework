from typing import List, Tuple

import pytest

from src.widget import get_date, mask_account_card


# Фикстура с данными для маскировки
@pytest.fixture
def account_card_data() -> List[Tuple[str, str]]:
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305")
    ]


# Тесты для mask_account_card
@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output


# Тесты для get_date
@pytest.mark.parametrize("input_date, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-11-10T14:20:00.000000", "10.11.2023"),
])
def test_get_date(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output
