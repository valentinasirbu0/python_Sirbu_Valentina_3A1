def words_to_tuples(*lists):
    max_len = max(len(lst) for lst in lists)
    combined = []

    for i in range(max_len):
        combined.append(tuple(lst[i] if i < len(lst) else None for lst in lists))

    return combined


rs = words_to_tuples([1, 2, 3], [5, 6, 7], ["a", "b", "c"])
print(rs)
