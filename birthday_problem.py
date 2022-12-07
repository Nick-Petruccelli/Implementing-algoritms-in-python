import math
#Create a factorial function
def factorial(n):

    nlist = []
    for n in range(1,n+1):
        nlist.append(n)
    factorialtotal = math.prod(nlist)
    if n == 0:
        factorialtotal = 1
    return factorialtotal
#defign function to show probability of no two birthdays on same day.
def birthday_noclash(r):
    return ((factorial(365)/factorial(365-r))/365**r)
#Problems
print("Problem 1")
print("the Probability of no two people sharing a birthday in a group of 22 is ", birthday_noclash(22))
print("Problem 2")
print("Assuming there are 30 people in the class, the probability that no two people from the class share a birthday is", birthday_noclash(30))
print("problem 3")
n = 1
while birthday_noclash(n) > .01:
    n += 1
print("For the probability of not sharing a birthday to be less than 1% the group size must be", n)
