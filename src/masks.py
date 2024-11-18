def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты, оставляя первые и последние четыре цифры.
    """
    card_str = str(card_number)
    # Проверяем длину номера карты
    if len(card_str) != 16:
        raise ValueError("Card number must be 16 digits")
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета по правилу **XXXX.
    :param account_number: Номер счета в виде целого числа.
    :return: Маскированный номер счета в строковом формате.
    """
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
