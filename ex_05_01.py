#Program reads user input
#Once done is entered print out the total, count and average of the numbers inputed
#Use try and except if the user enters anything other than a number or done

list = []
i=0
value= None
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        ivalue = int(value)
    except:
        print('Invalid input')
        continue
    i = i + 1
    list.append(ivalue)
total = sum(list)
print(total, i, (total/i))
