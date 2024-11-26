import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency, expected_result",
    [
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}}}
            ],
            "USD",
            [{"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
             {"id": 3, "operationAmount": {"currency": {"code": "USD"}}}]
        ),
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "RUB"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}}
            ],
            "USD",
            []
        ),
        ([], "USD", []),
    ]
)
def test_filter_by_currency(transactions, currency, expected_result):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected_result


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [{"description": "Перевод организации"},
             {"description": "Перевод со счета на счет"}],
            ["Перевод организации", "Перевод со счета на счет"]
        ),
        (
            [],
            []
        ),
        (
            [{"description": "Пополнение счета"}],
            ["Пополнение счета"]
        )
    ]
)
def test_transaction_descriptions(transactions, expected_descriptions):
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (5, 5, ["0000 0000 0000 0005"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ]
)
def test_card_number_generator(start, stop, expected_numbers):
    result = list(card_number_generator(start, stop))
    assert result == expected_numbers
