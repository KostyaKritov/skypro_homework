import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2022-01-01T00:00:00.000000",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Payment for service"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2022-02-01T00:00:00.000000",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Payment for goods"
        },
    ]


def test_filter_by_currency(transactions):
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["operationAmount"]["currency"]["code"] == "USD"

    rub_transactions = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["operationAmount"]["currency"]["code"] == "RUB"

    no_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(no_transactions) == 0


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == ["Payment for service", "Payment for goods"]

    empty_descriptions = list(transaction_descriptions([]))
    assert empty_descriptions == []


def test_card_number_generator():
    card_numbers = list(card_number_generator(1, 5))
    assert card_numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    single_card = list(card_number_generator(100, 100))
    assert single_card == ["0000 0000 0000 0100"]
