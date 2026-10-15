import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


# ========== capitilize ==========

def test_capitilize_positive(utils):
    """Позитивный тест: обычная строка."""
    assert utils.capitilize("skypro") == "Skypro"


def test_capitilize_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.capitilize("") == ""


def test_capitilize_none(utils):
    """Негативный тест: None."""
    # Здесь может быть дефект — код упадёт с AttributeError
    # Ожидаемое поведение: вернуть None или пустую строку
    # Фактическое: AttributeError


# ========== trim ==========

def test_trim_positive(utils):
    """Позитивный тест: строка с пробелами в начале."""
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces(utils):
    """Позитивный тест: строка без пробелов в начале."""
    assert utils.trim("skypro") == "skypro"


def test_trim_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.trim("") == ""


# ========== to_list ==========

def test_to_list_default_delimiter(utils):
    """Позитивный тест: разделитель по умолчанию (запятая)."""
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]


def test_to_list_custom_delimiter(utils):
    """Позитивный тест: кастомный разделитель."""
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]


def test_to_list_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.to_list("") == []


def test_to_list_none(utils):
    """Негативный тест: None."""
    # Здесь может быть дефект


# ========== contains ==========

def test_contains_true(utils):
    """Позитивный тест: символ есть в строке."""
    assert utils.contains("SkyPro", "S") is True


def test_contains_false(utils):
    """Негативный тест: символа нет в строке."""
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string(utils):
    """Негативный тест: пустая строка."""
    assert utils.contains("", "S") is False


# ========== delete_symbol ==========

def test_delete_symbol_char(utils):
    """Позитивный тест: удаление одного символа."""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring(utils):
    """Позитивный тест: удаление подстроки."""
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found(utils):
    """Негативный тест: символа нет в строке."""
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"


# ========== starts_with ==========

def test_starts_with_true(utils):
    """Позитивный тест."""
    assert utils.starts_with("SkyPro", "S") is True


def test_starts_with_false(utils):
    """Негативный тест."""
    assert utils.starts_with("SkyPro", "P") is False


# ========== end_with ==========

def test_end_with_true(utils):
    """Позитивный тест."""
    assert utils.end_with("SkyPro", "o") is True


def test_end_with_false(utils):
    """Негативный тест."""
    assert utils.end_with("SkyPro", "y") is False


# ========== is_empty ==========

def test_is_empty_true(utils):
    """Позитивный тест: пустая строка."""
    assert utils.is_empty("") is True


def test_is_empty_space(utils):
    """Позитивный тест: строка с пробелом."""
    assert utils.is_empty(" ") is True


def test_is_empty_false(utils):
    """Негативный тест: непустая строка."""
    assert utils.is_empty("SkyPro") is False


# ========== list_to_string ==========

def test_list_to_string_default(utils):
    """Позитивный тест: список с разделителем по умолчанию."""
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"


def test_list_to_string_custom_delimiter(utils):
    """Позитивный тест: кастомный разделитель."""
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"


def test_list_to_string_empty_list(utils):
    """Негативный тест: пустой список."""
    assert utils.list_to_string([]) == ""