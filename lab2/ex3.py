
def intersection(l1, l2):
    result = []
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            if l1[i] == l2[j]:
                result.append(l1[i])
    return result


def reunited(l1, l2):
    result = l1 + l2  # Concatenate the two lists
    return list(set(result))


def difference(l1, l2):
    result = []
    for num in l1:
        if num not in l2:
            result.append(num)
    return result


def test_lists(l1, l2):
    print(intersection(l1, l2))
    print(reunited(l1, l2))
    print(difference(l1, l2))
    print(difference(l2, l1))
    return 0


list_1 = [1, 2, 3]
list_2 = [2]
r = test_lists(list_1, list_2)
