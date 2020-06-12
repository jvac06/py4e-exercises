#Program reads user input
#Once done is entered print out the total, count and average of the numbers inputed
#Use try and except if the user enters anything other than a number or done

lista = []
i=0
value= None
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        ivalue = float(value)
    except:
        print('Invalid input')
        continue
    lista.append(ivalue)
maximum = max(lista)
minimum = min(lista)
print('Maximum:', maximum)
print('Minimum', minimum)
