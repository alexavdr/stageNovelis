"""
Exercise 4. Write a function to return True if the first and last number of a given list is same.
If numbers are different then return False.
"""

from typing import List


def is_same(my_list: List):
    """
    if the first and last item on the list are the same, it returns True. If they are different it returns False
    :param my_list: list
    :return: bool
    """
    if type(my_list) == list:
        return True if my_list[0] == my_list[-1] else False
    return "You did not enter a list!"


if __name__ == "__main__":
    test_list = [1, 2, 4.8, 55, 454, "hello", 2, " ", " "]
    print(is_same(test_list))
