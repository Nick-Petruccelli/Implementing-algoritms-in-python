import math
def triangular(n):
     i = int(n)
     trinum = (i*(i+1))//2
     return trinum
def sumupto(n2):
    x = 1
    sumtotal = 0
    while x < n2+1:
        sumtotal += x
        x = x + 1
    return sumtotal
def sumpower(n3,k):
    x2 = 1
    sumtotal2 = 0
    while x2 < n3+1:
        sumtotal2 += x2**k
        x2 = x2 + 1
    return sumtotal2
print("Problem 1")
for n in range(1,101):
    trinum = triangular(n)
    sumtotal = sumupto(n)
    print("n =",n,"Tn =",trinum,"Sn =",sumtotal)
print("Problem 2")
print("Conjecture: based on the first 100 n i think that Tn and Sn are equal.")
print("Problem 3")
Tnsum = 0
for n in range(1,21):
    Tnsum = triangular(n) + triangular(n-1)
    print(Tnsum)
print("Conjecture: based on the first 20 n Tn + Tn-1 seems to beequal to n^2.")
print("Problem 4")
pwsum = sumpower(2016,5)
print("sum 1^5+2^5+...+2016^5 =",pwsum)
print("Problem 5")
print("sumpower(100,-2) computes the sum of the first 100 integers to the -2 power.")
print("Problem 6")
sumpw1 = sumpower(500,-2)
sumpw2 = sumpower(5000,-2)
sumpw3 = sumpower(50000,-2)
print("sumpower(500,-2) =",sumpw1)
print("sumpower(5000,-2) =",sumpw2)
print("sumpower(50000,-2) =",sumpw3)
print("pi^2/6 =", (math.pi**2)/6)
print("With these comutations one could reasonable assume that 1^-2+2^-2+...+n^-2 where n is infity could equal pi^2/6 because our sumpower function seems to converge to pi^2/6 when the power is -2.")
