# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def count_occurrences(str1, str2):
    occurrences = str1.count(str2)

    return occurrences


result = count_occurrences("Valentina are mere, are bomboane, are note bune", "are")
print(result)

