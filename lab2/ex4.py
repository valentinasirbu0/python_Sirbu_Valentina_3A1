
def compose(notes, moves, start):
    result = []
    result.append(notes[start])
    i = 0
    while i < len(moves):
        start = start + moves[i]
        start = (start + len(notes)) % len(notes)
        result.append(notes[start])
        i += 1
    return result


r = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
print(r)
