#program reads file convert and prints lower letters in decreasing order
#of frequency, disregards whitespaces, digits and punctuation
import string

fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File not found:', fname)

counts = dict()
for line in fh:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.translate(str.maketrans('','',string.digits))
    line = line.translate(str.maketrans('','',string.whitespace))
    line = line.lower()
    # print('Debug', words)
    for ltr in line:
        counts[ltr] = counts.get(ltr,0)+1

#decorate: use of for iteration to create list of tuples and order them
lst = list()
for ltr, value in list(counts.items()):
    lst.append((value, ltr))
#sort
lst.sort(reverse=True)
#undecorate
for value, ltr in lst:
    print(ltr, value)
