import pytest

@pytest.fixture
def сlass_fixt():
    print('Перед каждым тестом запускается этот')
    print('сlass_fixt started')

@pytest.mark.usefixtures('сlass_fixt')
class TestSomething:
    def test_3(self):
        print('\ntest_3 started')

    def test_4(self):
        print('\ntest_4 started')
