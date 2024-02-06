
def factorial(n: int):
    """
    returns the factorial of a number
    :param n: number used to calculate factorial
    :return: int
    """
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


if __name__ == "__main__":
    print(factorial(5))
