def make_dictionary(stringg):
    dictionary = {}
    for char in stringg:
        if char not in dictionary.keys():
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary


r = make_dictionary("Ana has apples.")
print(r)

