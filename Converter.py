#!/usr/bin/env python3

class Converter():

    values = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}

    def __init__(self):
        pass

    def _convert_literal(self, l):
        """
        Convert literal l to decimal
        :param l: Roman literal
        :type l: str
        :return: Decimal value of l
        :rtype: int
        :raises:
            ValueError: when the given literal is not a roman literal
            TypeError: when l is not of type string
        """
        if type(l) is not str:
            raise TypeError('{} is not a valid roman literal'.format(l))
        try:
            return self.values[l]
        except KeyError:
            raise ValueError('{} is not a valid roman literal'.format(l))

    def convert(self, num):
        """
        Convert a string containing roman numerals to a decimal number
        :param num: string containing roman numerals
        :type num: str
        :return: decimal number with the same value as given numeral string
        :rtype: int
        """

        try:
            num = list(num)
        except TypeError:
            raise TypeError
        value = self._convert_literal(num[-1])
        for current, next in zip(num, num[1:]):
            if self._convert_literal(next) > self._convert_literal(current):
                value -= 2 * self._convert_literal(current)
            value += self._convert_literal(current)
        return value
