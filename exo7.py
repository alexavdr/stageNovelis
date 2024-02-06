"""
Exercise 7. Print the following pattern.

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def print_triangle():
    """
    Prints a number n followed by a space n times for numbers 1 to 5
    :return:
    """
    for i in range(1, 6):
        print((str(i)+" ")*i)


if __name__ == "__main__":
    print_triangle()
