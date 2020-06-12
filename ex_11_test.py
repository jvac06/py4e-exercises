import re

filename = "regex_sum_292452.txt"

fh =  open(filename)

numlist = list()
for line in fh:
    line = line.rstrip()
    inst = re.findall('[0-9]+', line)
    for e in range(len(inst)):
        num = int(inst[e])
        numlist.append(num)
print(sum(numlist))
