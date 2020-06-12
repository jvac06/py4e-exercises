#prompt user for hours and hourly rate.
#Pay 1.5rate for hours above 40
#Use 45 hours and 10.50 as rate
hrs = input("Enter Hours: ")
try:
    h = float(hrs)
except:
    print('Error, please enter numeric value')
    quit()

rate = input("Enter Rate: ")
try:
    r = float(rate)
except:
    print('Error, please enter numeric value')
    quit()

pay =  h * r

if h <= 40:
    print(pay)
else:
    pay = 40 * r
    overtime = h - 40
    rovertime = 1.5 * r
    otpay = overtime * rovertime
    totalpay = pay + otpay
    print(totalpay)
