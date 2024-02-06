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
    try:
        if 0 <= n < len(word):
            return word[n:]
        return ("The second parameter has to be a number greater than or equal to 0 and "
                "smaller than the length of the string")
    except TypeError:
        return "Input submitted was not the right type"
    except:
        return "Something went wrong"


if __name__ == "__main__":
    print(remove_char("python", -1))
