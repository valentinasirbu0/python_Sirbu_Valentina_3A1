
def find_in_lists(num, *lists):
    my_dict = {}
    index = 0
    for lst in lists:
        index += 1
        for key in lst:
            if key not in my_dict:
                my_dict[key] = str(index)
            else:
                my_dict[key] = str(my_dict[key]) + str(index)  # Update the value associated with the key

    keys_to_delete = []
    for word in my_dict:
        if len(my_dict[word]) != num:
            keys_to_delete.append(word)

    for key in keys_to_delete:
        del my_dict[key]

    return my_dict


r = find_in_lists(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
print(r)
