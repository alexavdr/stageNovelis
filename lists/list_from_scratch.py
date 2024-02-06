from typing import List


def union_with_rep(list1: List, list2: List):
    """
    adds two lists together (includes repetitions)
    :param list1: List
    :param list2: List
    :return: list
    """
    for item in list2:
        list1.append(item)
    return list1


def union_without_rep(list1: List, list2: List):
    """
    returns a new list with all items in list1 and list2 (without repetitions)
    :param list1: List
    :param list2: List
    :return: List
    """
    new_list = []
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    for item in list2:
        if item not in new_list:
            new_list.append(item)
    return new_list


def inter(list1: List, list2: List):
    """
    returns a new list with items found in list 1 and list 2
    :param list1: List
    :param list2: List
    :return: List
    """
    new_list = []
    for item in list1:
        if item in list2:
            new_list.append(item)
    return new_list


if __name__ == "__main__":
    list_1 = [1, 2, 3, 2, 4, 5, 6]
    list_2 = [4, 5, 6, 7, 8, 8]
    print(union_with_rep([1, 2, 3, 2, 4, 5, 6], [4, 5, 6, 7, 8, 8]))
    print(union_without_rep([1, 2, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 8]))
    print(inter([1, 2, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 8]))
    print(list_1 + list_2)

