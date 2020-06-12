#Write an edited program that will 'From' lines,
#find and print the days, guard against lines that
#start with from but only have one word
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
        print(words[2])
