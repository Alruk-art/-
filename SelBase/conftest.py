#общая фикстура для других тестов
import pytest

@pytest.fixture
def data_2():
    return 2


@pytest.fixture
def data_3():
    return 3

@pytest.fixture
def wide_use():
    print('\nШирокоиспользуемое')
    return "Проверено"
