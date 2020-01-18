#program categorizes logs email by sender
# and prints a dict() with count values
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File not found', fname)
counts = dict()
days = list()
for line in fh:
    words = line.split()
    # print('Debug', words)
    if len(words) >= 2 and words[0] == 'From':
        word = words[1]
        counts[word] = counts.get(word,0)+1
        # if word not in counts:
        #     counts[word] = 1
        # else:
            # counts[word] +=1
print(counts)
