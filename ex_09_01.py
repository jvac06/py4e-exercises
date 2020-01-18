#Program reads words in file, stores them in a dict() and uses in operator
#to check if a string is in a file.
fname = input('Enter file name: ')
w_name = input('Enter word you are seeking: ')
fh = open(fname)
r_inp = fh.read()
words = r_inp.split()
# print(type(words))
# print(len(words))
indice = {words[i]: i for i in range(0,len(words))}
# print(indice)
def search_w(word, dic):
    return word in dic

print(search_w(w_name, indice))
