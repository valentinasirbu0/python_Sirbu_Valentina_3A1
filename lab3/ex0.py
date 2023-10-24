#Cate cuvinte contine fisierul 'intrare.txt', un cuvant este format doar din litere A-Z, a-z cu lungime cel putin 1

def nr_cuvinte(content):
    print(content)
    words = content.split()
    num_words = len(words)
    return num_words


f = open("demofile.txt", "r")
print(nr_cuvinte(f.read()))