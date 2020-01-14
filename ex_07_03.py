#Write an Easter Egg code if someone writes na na boo boo as file name
fname = input('Enter file name: ')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhandle = open(fname)
except:
    print('File name is not recognized', fname)
    exit()

count = 0
for line in fhandle:
    line = line.rstrip()
    line = line.casefold()
    if line.startswith('subject:'):
        count = count + 1

print('There were %d subject lines in %s' %(count, fname))
