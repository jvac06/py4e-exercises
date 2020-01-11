#Write a program to read through a file and print the contents of the file (line by line) all in uppercase
fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File name is not recognized')
    exit()
for line in fhandle:
    line = line.rstrip()
    print(line.upper())
