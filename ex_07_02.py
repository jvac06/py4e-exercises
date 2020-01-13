#Write a program to read through a file for all the confidence index that the email is spam and create an average
fname = input('Enter file name: ')
try:
    fhandle = open(fname)
except:
    print('File name is not recognized')
    exit()
count = 0
sum_conf = 0
for line in fhandle:
    line = line.rstrip()
    line = line.casefold()
    if line.startswith('x-dspam-confidence:'):
        # print(line)
        count = count + 1
        sbegin = line.find('0.')
        conf_no = line[sbegin:]
        # print(conf_no)
        conf_no = float(conf_no)
        sum_conf = sum_conf + conf_no
        # print(count)
        # print(sum_conf)
avg = sum_conf/count
print('Confidence email spam average:', avg)