from typing import List, Tuple

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Фикстуры для маскировки данных
@pytest.fixture
def card_numbers() -> List[Tuple[int, str]]:
    return [
        (7000792289606361, "7000 79** **** 6361"),
        (1111222233334444, "1111 22** **** 4444")
    ]


@pytest.fixture
def account_numbers() -> List[Tuple[int, str]]:
    return [
        (73654108430135874305, "**4305"),
        (12345678, "**5678")
    ]


# Тесты для get_mask_card_number
@pytest.mark.parametrize("number, masked", [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567890123456, "1234 56** **** 3456"),
])
def test_get_mask_card_number(number: int, masked: str) -> None:
    assert get_mask_card_number(number) == masked


# Тесты для get_mask_account
@pytest.mark.parametrize("number, masked", [
    (73654108430135874305, "**4305"),
    (12345678, "**5678"),
])
def test_get_mask_account(number: int, masked: str) -> None:
    assert get_mask_account(number) == masked
