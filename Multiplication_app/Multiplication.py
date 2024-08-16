# Goal: to create a class which can perform the product of two numbers
# How: create a class with a method which takes two numbers as inputs and returns the product of the two numbers.


class Multiplication:
    def __init__(self):
        pass

    def _multiply_two_numbers(self, number1, number2):
        """
        multiply two numbers and return product

        :param number1: This is the first number for multiplication
        :param number2: This is the second number for multiplication
        :type number1: int
        :type number2: int
        :return product: The product of number1 and number2
        :rtype: int
        """
        product = number1 * number2
        return product
