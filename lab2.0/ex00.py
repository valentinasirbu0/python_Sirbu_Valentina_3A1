def ex00():
    L = [" ".join(bin(n)[2:].rjust(8, '0')) for n in range(9)]
    K = [bin(n)[2:].rjust(8, '0') for n in range(256)]
    print(L)
    print(K)


def ex000():
    try:
        x = 7.5 + 'hello'
    except:
        pass
    print("am trecut")


def ex0000():
    a = 10 + 100
    b = [1, 2, 3]
    c = a + b[0]
    while True:
        c = c + 1
        if c == 1050:
            print(abc)
            break
        elif c == 1000:
            abc = 1


#0
def ex0(n):
    sum = 0
    for x in range(n+1):
        sum += x
    return sum


#1
def liter_successive_ex1():
    return(" ".join(hex(n)[2:] for n in range(ord('0'), ord('9'))))

#chr(int(result[0])*13+int(result[1])) verificarea
r = liter_successive_ex1()


#2
def ex2():
    L = [" ".join(bin(n)[2:].rjust(8, '0')) for n in range(4+1)]
    zeroes = 0
    unos = 0
    for number in L:
        zeroes += number.count('0')
        unos += number.count('1')
    print(zeroes)
    print(unos)


#3
def ex3():
    print(f"{5/3:.100f}")




#4
import numpy as np

def rezolva_sistem(a, b, c, d, e):
    coeficienti = np.array([a, b, c, d])
    termeni_liberi = np.array(e)

    solutie = np.linalg.solve(coeficienti, termeni_liberi)

    return solutie

a = [2, 3, -1, 1] #necunoscute x,y,z,t
b = [3, -2, 2, 1]
c = [1, -1, 1, -3]
d = [4, -1, 3, -1]
e = [5, 10, -2, 8] #rezultate a=5 s.a.m.d

solutii = rezolva_sistem(a, b, c, d, e)

print("Solutiile sistemului sunt:")
for i, solutie in enumerate(solutii):
    print(f"Necunoscuta {i + 1}: {solutie}")




#5
def nth_root_integer_only(x, n, precision=50):
    # initializam variabile
    p = 0
    result = 0

    for _ in range(precision):
        # cautam x maxim a.i. y <= c
        c = 10 * (x + result * result ** (n - 1))
        y = 0

        for d in range(1, 11):
            if d * (p * 10 + d) ** (n - 1) <= c:
                y = d
            else:
                break

        # lipim x la rezultat
        result = result * 10 + y
        p = p * 10 + y

        # update restul
        c = c - y * (p - 1) ** (n - 1)

        # restul este 0
        if c == 0:
            break

    return result


x = 12345678901234567890123456789012345678901234567890
n = 4  #radacina
precision = 50  #zecimale

#result = nth_root_integer_only(x, n, precision)
#print(f"The {n}-th root of {x} with {precision} decimal places is approximately: {result}")


#6
import itertools
def generate_permutations(alphabet, n, p):
    if n >= len(alphabet) ** p:
        return []  # Nu există suficiente permutări

    words = []
    for perm in itertools.product(alphabet, repeat=p):
        words.append("".join(perm))
        if len(words) == n:
            break

    return words


alphabet = "abc"
n = 10  # Numărul de permutări dorit
p = 3  # Lungimea cuvintelor

permutations = generate_permutations(alphabet, n, p)
#print(f"Primele {n} permutări de {p} litere din alfabetul '{alphabet}':")
#for word in permutations:
#    print(word)


#7
def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(8)

hex_strings = [
    "0x00", "0x00", "0xFC", "0x66", "0x66", "0x66", "0x7C", "0x60",
    "0x60", "0x60", "0x60", "0xF0", "0x00", "0x00", "0x00", "0x00",
    "0x00", "0x00", "0x00", "0x00", "0x00", "0xC6", "0xC6", "0xC6",
    "0xC6", "0xC6", "0xC6", "0x7E", "0x06", "0x0C", "0xF8", "0x00",
    "0x00", "0x00", "0x10", "0x30", "0x30", "0xFC", "0x30", "0x30",
    "0x30", "0x30", "0x36", "0x1C", "0x00", "0x00", "0x00", "0x00",
    "0x00", "0x00", "0xE0", "0x60", "0x60", "0x6C", "0x76", "0x66",
    "0x66", "0x66", "0x66", "0xE6", "0x00", "0x00", "0x00", "0x00",
    "0x00", "0x00", "0x00", "0x00", "0x00", "0x7C", "0xC6", "0xC6",
    "0xC6", "0xC6", "0xC6", "0x7C", "0x00", "0x00", "0x00", "0x00",
    "0x00", "0x00", "0x00", "0x00", "0x00", "0xDC", "0x66", "0x66",
    "0x66", "0x66", "0x66", "0x66", "0x00", "0x00", "0x00", "0x00"
]


#for i in range(0, len(hex_strings), 8):
#    matrix = [hex_to_binary(hex_strings[j]) for j in range(i, i + 8)]
#    print("\n".join(matrix))
#    print()


#8
def calculeaza_aria(Y):
    n = len(Y)
    if n <= 1:
        return 0

    dx = 1  # intervalul pe x
    aria = 0

    for i in range(n - 1):
        y1, y2 = Y[i], Y[i + 1]
        aria += min(y1, y2) * dx

    return aria


Y = [1, 3, 2, 4, 1, 2]
aria = calculeaza_aria(Y)
#print(f"Aria aproximativă a suprafeței este: {aria}")
