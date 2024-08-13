# Goal: create a clss which can preform subtraction of two numbers
# How: create a class with a method which takes two numbers as input and returns the difference of the numbers


class Subtraction:
    def __init__(self):
        pass

    def sub_two_nums(self, num1: int, num2: int):
        """
        Subtract two numbers and return difference

        :param num1: This is the first number for subtraction
        :param num2: This is the second number for subtraction
        :type num1: int
        :type num2: int
        :return difference: The difference of num1 and num2
        :rtype: int
        """
        diff = num1 - num2
        return diff
