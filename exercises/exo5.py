"""
Exercise 5. Iterate the given list of numbers and print only those numbers which are divisible by 5.
"""
from typing import List


def div_5(my_list: List):
    """
    iterates through the list of numbers. If the number modulo 5 is equal to 0, then the number is printed
    :param my_list:
    :return:
    """
    if type(my_list) == list and len(my_list) > 0:
        for item in my_list:
            try:
                if item % 5 == 0:
                    print(item)
            except TypeError:
                pass
    else:
        print("You did not enter a list or it is empty!")


if __name__ == "__main__":
    div_5([])

