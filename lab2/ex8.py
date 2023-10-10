def convert_to_ascii(x=1, lists=None, flag=True):
    final_result = []
    for string in lists:
        result = []
        for char in string:
            if (flag and ord(char) % x == 0) or (not flag and ord(char) % x != 0):
                result.append(char)
        final_result.append(result)
    return final_result


r = convert_to_ascii(2, ["test", "hello", "lab002"], False)
print(r)
