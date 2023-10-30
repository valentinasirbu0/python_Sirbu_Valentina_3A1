
def find_loop(dictionary):
    visited = []
    key = 'start'

    while key not in visited:
        if key != 'start':
            visited.append(key)
        next_key = dictionary.get(key, None)
        if next_key is not None:
            key = next_key
        else:
            break

    return visited



r = find_loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
print(r)
