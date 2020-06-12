#program reads file convert and prints lower letters in decreasing order
#of frequency, disregards whitespaces, digits and punctuation
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
        time = words[5].split(':')
        hour = time[0]
        counts[hour] = counts.get(hour,0)+1

#decorate: use of for iteration to create list of tuples and order them
lst = list(counts.items())
#sort
lst.sort()
#undecorate
for key, value in lst:
    print(key, value)
