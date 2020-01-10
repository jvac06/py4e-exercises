#Create score range; if out of range give error message
score = input("Enter Score between 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print('Bad score')
    quit()

if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6 and score >= 0.0:
        print('F')
else:
    print('Score provided is out of range.')
