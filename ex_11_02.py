import re

fname = input("Enter filename: ")

try:
    fh = open(fname)
except:
    print(fname, "not found")

numlist = list()
for line in fh:
    line = line.rstrip()
    results = re.findall('New.*: ([0-9]+)', line)
    if len(results) != 1: continue
    num = float(results[0])
    numlist.append(num)
print(sum(numlist)/len(numlist))
