#!/usr/bin/env python3

class Converter():

    values = {'I' : 1,
              'V' : 5,
              'X' : 10,
              'L' : 50,
              'C' : 100,
              'D' : 500,
              'M' : 1000}

    def __init__(self):
        pass

    def convert(self, num):
        """
        Convert a string containing roman numerals to a decimal number
        :param num: string containing roman numerals
        :type num: str
        :return: decimal number with the same value as given numeral string
        :rtype: int
        """

        num = list(num)
        value = Converter.values[num[-1]]
        for current, next in zip(num, num[1:]):
            if Converter.values[next] > Converter.values[current]:
                value -= 2*Converter.values[current]
            value += Converter.values[current]
        return value
