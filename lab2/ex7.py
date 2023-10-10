def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


def palindromes(lists):
    palindrome = []
    for number in lists:
        if is_palindrome(number):
            palindrome.append(str(number))
    return palindrome, max(palindrome, key=len)


r = palindromes([1221, 145, 985, 61, 5, 33, 2452, 666, 658])
print(r)
