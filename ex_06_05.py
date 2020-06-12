text = "X-DSPAM-Confidence:    0.8475"
str_start = text.find(':')
slice = text[str_start+4:]
# print(str_start)
flt = float(slice)
print(flt)
