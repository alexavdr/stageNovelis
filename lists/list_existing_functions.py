from typing import List


def union_with_rep(list1: List, list2: List):
    return list1 + list2


def union_without_rep(list1: List, list2: List):
    return list(set(list1 + list2))


def inter(list1: List, list2: List):
    #return list(set(list1) & set(list2))
    return set(list1).intersection(list2)


if __name__ == "__main__":
    list_1 = [1, 2, 3, 2, 4, 5, 6]
    list_2 = [4, 5, 6, 7, 8, 8]
    print(union_with_rep([1, 2, 3, 2, 4, 5, 6], [4, 5, 6, 7, 8, 8]))
    print(union_without_rep([1, 2, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 8]))
    print(inter([1, 2, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 8]))
