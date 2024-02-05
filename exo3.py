"""
Exercise 3. Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

· remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.

· remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
"""


def remove_char(word: str, n: int):
    """
    returns the string "word" without the first n characters
    :param word: string
    :param n: int
    :return:
    """
    return word[n:]


if __name__ == "__main__":
    string, i = input("String: "), int(input("Number: "))
    print(remove_char(string, i))
