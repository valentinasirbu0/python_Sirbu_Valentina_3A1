def count_matching_values(*args, **kwargs):
    keyword_values = set(kwargs.values())
    count = sum(1 for arg in args if arg in keyword_values)

    return count


result = count_matching_values(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
