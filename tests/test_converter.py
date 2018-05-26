import unittest

from Converter import Converter


class TestSingleNumerals(unittest.TestCase):
    """
    Test all single numerals IVXLCDM
    """

    input_output = [(num, dec) for num, dec in zip(list('IVXLCDM'), [1, 5, 10, 50, 100, 500])]

    def myAssertEqual(self, num, dec):
        self.assertEqual(self.c.convert(num), dec)

    def setUp(self):
        self.c = Converter()

    def test_list(self):
        for input, output in self.input_output:
            with self.subTest(input=input, output=output):
                self.assertEqual(self.c.convert(input), output)


class TestSimpleCombinations(unittest.TestCase):
    """
    Test simple combinations which only require addition
    """

    def setUp(self):
        self.c = Converter();

    def test_numeral_ii(self):
        self.assertEqual(self.c.convert('II'), 2)

    def test_numeral_vii(self):
        self.assertEqual(self.c.convert('MDCLXVI'), 1666)

    def test_numeral(self):
        self.assertEqual(self.c.convert(('MMXVIII')), 2018)

class TestSubtractiveCombinations(unittest.TestCase):

    def setUp(self):
        self.c = Converter()

    def test_numeral_iv(self):
        self.assertEqual(self.c.convert('IV'), 4)

    def test_numeral_cd(self):
        self.assertEqual(self.c.convert('CD'), 400)

    def test_numeral_lxix(self):
        self.assertEqual(self.c.convert('LXIX'), 69)

    def test_numeral_mmmcxcii(self):
        self.assertEqual(self.c.convert('MMMCXCII'), 3192)

class TestInvalidInput(unittest.TestCase):

    def setUp(self):
        self.c = Converter()

    def test_digit(self):
        with self.assertRaises(TypeError):
            self.c.convert(6)

    def test_number(self):
        with self.assertRaises(TypeError):
            self.c.convert(314)

    def test_invalid_literals(self):
        with self.assertRaises(ValueError):
            self.c.convert('UI')

    def test_objects(self):
        with self.assertRaises(TypeError):
            self.c.convert(object())


if __name__ == '__main__':
    unittest.main()