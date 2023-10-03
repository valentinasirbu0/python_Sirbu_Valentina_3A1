# Write a script that calculates how many vowels are in a string.

def find_vow(str):
    vowels = "aeiouAEIOU"
    count = 0
    for x in str:
        if x in vowels:
            count+= 1
    return count        

print(find_vow("Valentina"))