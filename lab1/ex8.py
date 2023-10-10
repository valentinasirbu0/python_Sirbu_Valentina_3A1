#Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def count_set_bits(number):
    count = 0

    while number:
        count += number & 1
        number >>= 1

    return count


# Example usage:
number = 24
bit_count = count_set_bits(number)
print(f"Number of set bits in {number}: {bit_count}")
