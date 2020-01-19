#program categorizes logs email by domain name
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
        e_address = words[1]
        sbeg = e_address.find('@')
        # print('slice begins at index:', sbeg)
        dname = e_address[sbeg:]
        counts[dname] = counts.get(dname,0)+1

print(counts)
