import unittest

# Наш объект тестирования

from bubble_sort import bubble_sort
class BubbleSortTest(unittest.TestCase):

    def test_1(self):
        result = bubble_sort([7, 3, 6, 11, 2])
        self.assertEqual([
            1, 3, 6, 7, 11
            ],
            result
        )
        print(result)

    def test_2(self):
        result = bubble_sort([7, 3, 6, 2, 11])
        self.assertEqual(
            [2, 3, 6, 7, 11],
            result
            )

    def test_float(self):

        result = bubble_sort ([1.2, 3.4, -5.6])
        self.assertEqual([
            -5.6, 1.2, 3.4
            ],
            result
        )

    def test_string(self):
        result = bubble_sort([
            "banana",
            "apple",
            "огурец",
            "123"
        ])
        self.assertEqual(
            [
                "123",
                "apple",
                "banana",
                "огурец"
            ],
            result
        )

    def test_mix(self):
        result = bubble_sort([1, "sd", None])

    def test_проверяет_исключение_на_несовместимость_типов(self):
        with self.assertRaises(TypeError):
            result = bubble_sort([1, "sd", None])