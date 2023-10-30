
def intersection(args):
    if len(args) == 2:
        return args[0].intersection(args[1])
    else:
        result = args[0].intersection(intersection(args[1:]))
        return result


def reunited(args):
    if len(args) == 2:
        return args[0].union(args[1])
    else:
        result = args[0].union(reunited(args[1:]))
        return result


def difference(args):
    result = args[0].difference(args[1])
    return result



def test_sets(*args):
    arguments = list(args)
    print(arguments[0], "&", arguments[1], ": ", intersection(arguments))
    print(arguments[0], "|", arguments[1], ": ", reunited(arguments))
    print(arguments[0], "-", arguments[1], ": ", difference(arguments))
    print(arguments[0], "-", arguments[1], ": ", difference(list(reversed(arguments)))) #inverseaza lista
    return 0


#r = test_sets({1, 2}, {2, 3}, {5, 6})
r = test_sets({1, 2}, {2, 3})