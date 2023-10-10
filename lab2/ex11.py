def custom_sort(tuples):
    def sorting_key(item):
        if len(item[1]) >= 3:
            return item[1][2]
        return item[1]  # If the string is shorter than 3 characters, use the entire string

    sorted_tuples = sorted(tuples, key=sorting_key)
    return sorted_tuples


# Example input list of string tuples
input_tuples = [('abc', 'bcd'), ('abc', 'zza')]

result = custom_sort(input_tuples)
print(result)
