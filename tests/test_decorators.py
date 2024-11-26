import pytest

from src.decorators import log


@log()
def func_success(x, y):
    return x + y


@log()
def func_error(x, y):
    return x / y


@log(filename="test_log.txt")
def func_file_log(x, y):
    return x * y


def test_log_to_console(caplog):
    with caplog.at_level("INFO"):
        result = func_success(1, 2)
        assert result == 3

    assert "func_success started with inputs: (1, 2), {}" in caplog.text
    assert "func_success ok. Result: 3" in caplog.text


def test_log_error_handling(caplog):
    with caplog.at_level("INFO"):
        with pytest.raises(ZeroDivisionError):
            func_error(1, 0)

    assert "func_error started with inputs: (1, 0), {}" in caplog.text
    assert "func_error error: ZeroDivisionError. Inputs: (1, 0), {}" in caplog.text


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file)
    def multiply(a, b):
        return a * b

    multiply(2, 3)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert "multiply started with inputs: (2, 3), {}" in log_content
    assert "multiply ok. Result: 6" in log_content
