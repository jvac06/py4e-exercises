str = 'X-DSPAM-Confidence:0.8475'
str_start = str.find(':')
slice = str[str_start+1:-1]
# print(str_start)
flt = float(slice)
print(flt)
