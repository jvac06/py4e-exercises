#program categorizes logs email by sender
# and uses items method & tuples to print sender with most emails
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File not found:', fname)
counts = dict()

for line in fh:
    words = line.split()
    # print('Debug', words)
    if len(words) >= 2 and words[0] == 'From':
        word = words[1]
        counts[word] = counts.get(word,0)+1
#decorate: use of for iteration to create list of tuples and order them
lst = list()
for key, value in list(counts.items()):
    lst.append((value, key))
#sort
lst.sort(reverse=True)
#undecorate
value, key = lst[0]
print(key, value)
