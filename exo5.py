"""
Exercise 5. Iterate the given list of numbers and print only those numbers which are divisible by 5.
"""
from typing import List


def div_5(my_list: List):
    """
    iterates through the list of numbers. If the number is modulo 5 is equal to 0, then the number is orinted
    :param my_list:
    :return:
    """
    for item in my_list:
        if item % 5 == 0:
            print(item)


if __name__ == "__main__":
    div_5([2, 4, 6, 0, 5, 20, 4, 100])

