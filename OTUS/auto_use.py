import pytest

@pytest.fixture(autouse=True)
def autoanyname():
    print('\nНачало Auto_Use фикстура для всех тестов')


def test_01():
        print ('test_01 started')


def test_02():
    print ('test_02 started')