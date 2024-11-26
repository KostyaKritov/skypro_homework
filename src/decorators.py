import functools
import logging


def log(filename=None):
    """
    Декоратор для логирования выполнения функции.
    Логи записываются в файл (если задан `filename`) или выводятся в консоль.
    :param filename: Имя файла для логирования (опционально).
    """
    def decorator(func):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info(f"{func.__name__} started with inputs: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
        return wrapper
    return decorator
