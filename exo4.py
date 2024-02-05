"""
Exercise 4. Write a function to return True if the first and last number of a given list is same.
If numbers are different then return False.
"""


def is_same(my_list: list):
    """
    if the first and last item on the list are the same, it returns True. If they are different it returns False
    :param my_list: list
    :return: bool
    """
    return True if my_list[0] == my_list[-1] else False


if __name__ == "__main__":
    test_list = [1, 2, 4, 55, 454, 2, 2, 3, 1]
    print(is_same(test_list))
