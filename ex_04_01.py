import random

for i in range(10):
    x = random.random()
    print(x)

ranint = random.randint(1,100)
print(ranint)

list = [1,2,3,4,5,10,20,30,40,50]
choice1 = random.choice(list)
choice2 = random.choice(list)
print(choice1)
print(choice2)
