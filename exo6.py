"""
Exercise 6. Write a program to find how many times substring “Emma” appears in the given string.
"""
from typing import List


def emma_count(list_x: List):
    """
    iterates through each string in the list. If the string is equal to "Emma", variable "count" increases by 1.
    :param list_x: list
    :return: int
    """
    count = 0
    for word in list_x:
        count += 1 if word == "Emma" else 0
    return count


if __name__ == "__main__":
    str_x = input("String: ").split()
    print("Emma appeared {} times".format(emma_count(str_x)))
