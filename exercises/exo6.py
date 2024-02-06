"""
Exercise 6. Write a program to find how many times substring “Emma” appears in the given string.
"""


def emma_count(string: str):
    """
    iterates through each string in the list. If the string is equal to "Emma", variable "count" increases by 1.
    :param string: str
    :return: int
    """
    count = 0
    try:
        string = string.split()
        for word in string:
            count += 1 if word.lower() == "emma" else 0
        return count
    except:
        return "has to be a string!"


if __name__ == "__main__":
    str_x = input("String: ")
    print("Emma appeared {} times".format(emma_count(str_x)))
