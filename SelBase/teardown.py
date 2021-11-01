import pytest

@pytest.fixture
def fixt(request):
    print ('\nBegin in fixt')
    print(f'Call from {request.function.__name__}')
    yield
    print('\nRolling back in fixt')

@pytest.fixture
def fixt_fin(request):
    print('\nBegin in fixt_fin')
    print(f'Call from{request.function.__name__}')

    #def fin():
    #    print('\nRolling back in fixt_fin')
    #request.addfinalizer(fin)

def test_01(fixt):
    # print('\ntest_01 started') #gthdsq вариант прогона теста
    assert 1 == 1 # '0' для возникновения ошибки 1:11:20

def test_02(fixt):
    print('\ntest_02 started')