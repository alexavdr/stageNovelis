
"""
Exercise 1. Given two integer numbers, return their product only if the product is equal to or lower than 1000.
Otherwise, return their sum.
"""


def mul_sum(num1: int, num2: int):
    """
    Returns the product of two given integers if the product is smaller than or equal to 1000.
    If the product is greater than 1000 it returns the sum of both integers.
    :param num1: int
    :param num2: int
    :return: int
    """
    if num1*num2 <= 1000:
        return num1*num2
    return num1+num2


if __name__ == "__main__":
    num_1 = int(input("Number 1: "))
    num_2 = int(input("Number 2: "))
    print(mul_sum(num_1, num_2))
