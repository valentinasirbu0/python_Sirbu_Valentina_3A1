
def find_unique(list):
    unique = {elem for elem in list}
    return len(unique), len(list)-len(unique)

r = find_unique(["a", "a", "g", "c", "d", 3, "s", 2, 2, "h"])
print(r)