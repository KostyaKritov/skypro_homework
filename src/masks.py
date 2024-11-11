def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты по правилу XXXX XX** **** XXXX.
    :param card_number: Номер карты в виде целого числа.
    :return: Маскированный номер карты в строковом формате.
    """
    card_number_str = str(card_number)
    return f"XXXX XX** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета по правилу **XXXX.
    :param account_number: Номер счета в виде целого числа.
    :return: Маскированный номер счета в строковом формате.
    """
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
