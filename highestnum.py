


print("Pick 3 random numbers between 1 and 100.")
print("And I will tell which one is the highest.")
fnum = int(input('Pick your first number: '))
snum = int(input('Pick your second number: '))
tnum = int(input('Pick your third number: '))

hnum = fnum
if snum > hnum:
    hnum = snum
if tnum > hnum:
    hnum = tnum
