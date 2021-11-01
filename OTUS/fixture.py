# C:\pythonProjectNat\pytest_yt_OTUS
#  pytest -v fixture.py::test_data_1 --setup-show (для запуска из терминала)
# pytest -s fixture.py::test_data_1 --setup-show
# pytest -s fixture.py::test_wide_use (последний пример)

import pytest
# $ pytest --setup-show

@pytest.fixture
def data_1():
    return 1

@pytest.fixture
def print_start():
    # raise ConnectionError (для определения ошибки при подготовке или в самом файле
    print('\nПодготовка к тесту')

def test_data_1( print_start):
    pass
    #assert data_1 == 1

def test_data_2(data_2):
    assert data_2 == 2

def test_data_3(data_3):
    assert data_3 == 3


def test_wide_use(wide_use):
    assert wide_use == "Проверено"
