#Program reads through mail box data, splits lines, finds who sent the email
#and count the amount of senders
fname = input('Enter file name: ')

try:
    fhandle = open(fname)
except:
    print('File name is not recognized', fname)
    exit()

count = 0
for line in fhandle:
    words = line.split()
    # print('Debug:', words)
    if len(words) >= 2 and words[0] == 'From':
        count = count + 1
        print(words[1])
print('There were %d lines in the file with From as the first word' %count)
