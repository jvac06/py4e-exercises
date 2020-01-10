#Program reads user input
#Once done is entered print out the total, count and average of the numbers inputed
#Use try and except if the user enters anything other than a number or done
#i = 0
largest = None
smallest = None
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        ivalue = int(value)
    except:
        print('Invalid input')
        continue
    #i = i + 1
    if largest == None:
        largest = ivalue
    if smallest == None:
        smallest = ivalue
    if ivalue > largest:
        largest = ivalue
    if ivalue < smallest:
        smallest = ivalue
print('Maximum is', largest)
print('Minimum is', smallest)
