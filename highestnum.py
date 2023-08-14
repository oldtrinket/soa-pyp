#In this code, I first initialize the variable highest to the value of fnum.
#Then, I use the if statements to check if snum and tnum are greater than highest. If they are,
#then I update the value of highest to the new value. Finally, I print the value of highest.
#This code will now only print the highest number among the three random numbers

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
