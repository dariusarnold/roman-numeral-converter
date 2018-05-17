import unittest

from Converter import Converter

input_output = [(num, dec) for num, dec in zip(list('IVXLCDM'), [1, 5, 10, 50, 100, 500])]

class TestSingleNumerals(unittest.TestCase):
    """
    Test all single numerals IVXLCDM
    """

    def myAssertEqual(self, num, dec):
        self.assertEqual(self.c.convert(num), dec)

    def setUp(self):
        self.c = Converter()

    def test_numeral_i(self):
        self.assertEqual(self.c.convert('I'), 1)

    def test_numeral_v(self):
        self.assertEqual(self.c.convert('V'), 5)

    def test_numeral_x(self):
        self.assertEqual(self.c.convert('X'), 10)

    def test_numeral_l(self):
        self.assertEqual(self.c.convert('L'), 50)

    def test_numeral_c(self):
        self.assertEqual(self.c.convert('C'), 100)

    def test_numeral_d(self):
        self.assertEqual(self.c.convert('D') , 500)

    def test_numeral_m(self):
        self.assertEqual(self.c.convert('M'), 1000)

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

if __name__ == '__main__':
    unittest.main()