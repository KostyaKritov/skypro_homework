# Проект Bank Widget

## Описание проекта

Этот проект представляет собой виджет для личного кабинета клиента банка. Виджет отображает последние операции, а также позволяет фильтровать и сортировать операции по заданным критериям.

## Установка

Склонируйте репозиторий:

   ```bash
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
