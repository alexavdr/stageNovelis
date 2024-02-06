
def is_palindrome(string: str):
    """
    Returns True if the given string is a palindrome. Otherwise, returns False.
    :param string: string used to check if it is a palindrome
    :return: bool
    """
    for i in range(0, int(len(string)/2)):
        if string[i] != string[-(i+1)]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("12"))
