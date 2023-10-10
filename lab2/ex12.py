def group_by_rhyme(words):
    result = []
    i = 0
    while i < len(words):
        rhymes = [words[i]]
        j = i + 1
        while j < len(words):
            if last_two_chars(words[i]) == last_two_chars(words[j]):
                rhymes.append(words[j])
                words.pop(j)
            else:
                j += 1
        result.append(rhymes)
        i += 1
    return result


def last_two_chars(word):
    return word[-2:]


# Example input list of words
w = ['ana', 'banana', 'carte', 'arme', 'parte']
r = group_by_rhyme(w)
print(r)
