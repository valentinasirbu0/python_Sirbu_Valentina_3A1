dict1 = {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
dict2 = {'a': 3, 's': 2, '.': 1, 'e': [1, 2, 3], 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}


def compare_dict(dic1, dic2):
    for key, value in dic1.items():
        if key in dic2 and dic2[key] == value:
            continue
        else:
            return False
    return True


r = compare_dict(dict1, dict2)
print(r)
