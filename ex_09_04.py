#program categorizes logs email by sender
# and uses max loop to print sender with most emails
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
# print(type(counts.values()))

largest = None
for e_count in list(counts.values()):
    if largest is None or e_count > largest:
        largest = e_count

for key in counts:
    if counts[key] == largest:
        print(key, counts[key])
# print(counts)
