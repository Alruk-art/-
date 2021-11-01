# видео https://www.youtube.com/watch?v=OVaKlTR87yk&t=43
import pytest
import sys
# C:\pythonProjectNat\pytest_yt_OTUS
# pytest -v test_02_mark.py::test_intersect (выборочный через терминал)

@pytest.mark.skip(reason='Skipped test example')

@pytest.mark.skipif(sys.version_info > (3, 5), reason = "requires" )
def test_skip_if():
    pass

@pytest.mark.xfail(reason='wrong comparison', strict=True)
def test_fail_comparison():
    assert 1 == 0

@pytest.mark.xfail(raises=(AssertionError, TimeoutError))
def test_fail_exception():
    raise AssertionError

def func(a):
     if a < 0:
          return 'negative'
     elif a == 0:
         return 'zero'
     elif a > 0:
         return 'positive'

@pytest.mark.parametrize('a, result', [
    (-1, 'negative'),
    (0, 'zerA'),
    (2, 'positive')
])
def test_all_cases(a, result):
    assert func(a) == result

@pytest.mark.parametrize('a', [1, 2])
@pytest.mark.parametrize('b', [3, 4])
def test_intersect(a, b):
    print (a, b)


