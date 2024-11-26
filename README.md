# Проект Bank Widget

## Описание проекта

Этот проект представляет собой виджет для личного кабинета клиента банка. Виджет отображает последние операции, а также позволяет фильтровать и сортировать операции по заданным критериям.

## Установка

Склонируйте репозиторий:

   ```
   git clone https://github.com/yourusername/your-repository-name.git
   cd your-repository-name
   ```
## Модули

### Модуль ***masks*** содержит функции для маскирования банковских данных.

Маскирует номер банковской карты, используя формат XXXX XX** **** XXXX.

Пример:

   ```
   from src.masks import get_mask_card_number

   masked_card = get_mask_card_number(7000792289606361)
   print(masked_card)  # "7000 79** **** 6361"
   ```

### Модуль ***widget*** содержит функции для работы с информацией о банковских картах и счетах.

***mask_account_card(info: str) -> str*** -
принимает строку с типом и номером карты или счета и возвращает строку с замаскированным номером. Использует функции из модуля masks.

Пример:

   ```
   from src.widget import mask_account_card

   result = mask_account_card("Visa Platinum 7000792289606361")
   print(result)  # "Visa Platinum 7000 79** **** 6361"
   ```

### Модуль ***processing*** содержит функции для обработки данных о банковских операциях.

***filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]*** - 
фильтрует список операций по состоянию. По умолчанию возвращает только операции с состоянием ***'EXECUTED'***.

Пример:

   ```
   from src.processing import filter_by_state

   data = [
      {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
   ]

   filtered_data = filter_by_state(data)
   print(filtered_data)  # [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
   ```

### Модуль ***generators*** содержит генераторы для обработки и работы с данными.

***filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]*** -
фильтрует список транзакций по заданной валюте и возвращает итератор. Удобно использовать для обработки больших объемов данных.

Пример:

   ```
    from src.generators import filter_by_currency

    transactions = [
        {
            "id": 939719570,
           "state": "EXECUTED",
           "operationAmount": {
               "currency": {"code": "USD"}
           }
        },
       {
          "id": 142264268,
          "state": "EXECUTED",
           "operationAmount": {
               "currency": {"code": "RUB"}
           }
        }
    ]

    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
        print(transaction)  # Выводит только транзакции с валютой "USD"
   ```

***transaction_descriptions(transactions: List[Dict]) -> Iterator[str]*** -
генерирует описание операций из списка транзакций.

Пример:

   ```
    from src.generators import transaction_descriptions

    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"}
    ]

    descriptions = transaction_descriptions(transactions)
    for description in descriptions:
        print(description)
    # Вывод:
    # Перевод организации
    # Перевод со счета на счет
   ```

***card_number_generator(start: int, stop: int) -> Iterator[str]*** -
генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

Пример:

   ```
   from src.generators import card_number_generator

    for card_number in card_number_generator(1, 3):
        print(card_number)
    # Вывод:
    # 0000 0000 0000 0001
    # 0000 0000 0000 0002
    # 0000 0000 0000 0003
   ```

### Модуль ***decorators*** содержит декоратор `log`.

***Декоратор `log`, который логирует начало и завершение работы функции, а также ошибки, если они возникают.***

Пример:

   ```
    python
    from src.decorators import log

    @log(filename="log.txt")
    def add(x, y):
        return x + y

    add(1, 2)  # Лог записывается в файл log.txt

    @log()
    def divide(x, y):
        return x / y

    divide(4, 2)  # Лог выводится в консоль
   ```

## Тестирование

Для запуска тестов используйте следующую команду:

   ```
    pytest .
   ```

### Отчёт тестирования находится в [htmlcov](htmlcov/index.html).
