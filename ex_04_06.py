#Use a function
#prompt user for hours and hourly rate.
#Pay 1.5 rate for hours above 40
#Use 45 hours and 10.50 as rate
def computepay(h,r):
    try:
        h = float(hrs)
        r = float(rate)
    except:
        print('Please enter numeric value')
        quit()
    regular = h * r
    if h > 40:
        otp = (h - 40) * (r * .5)
        totalpay = regular + otp
        return totalpay
    else:
        return regular

hrs = input("Enter Hours:")
rate = input("Enter rate: ")

p = computepay(hrs,rate)
print(p)
