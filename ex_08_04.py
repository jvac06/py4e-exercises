#Write a program to read a file line by line and add to a list if the word is not already on the list
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('Cannot find a file with this name', fname)

w_list = []
for line in fh:
    words = line.split()
    for w in words:
        if not w_list or w not in w_list:
            w_list.append(w)

w_list.sort()
print(w_list)
