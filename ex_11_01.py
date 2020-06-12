#program to mimic grep function in command line
import re

#ask for input
regex = input('Enter a regular expression: ')
#open File
filename = 'mbox.txt'
fh = open(filename)

count = 0
for line in fh:
    line  = line.rstrip()
    x = re.search(regex, line)
    if x:
        count += 1
if count > 0:
    print('{} had {} lines that matched {}'.format(filename, count, regex))
else:
    print('no lines matched')
