#Defining function f.
def f(n):
    if n%2 ==0:
        return n/2
    else:
        return 3*n+1
#Defigning the hailstone sequence.
def hailstone(n):
    hailstone_seq = [n]
    while hailstone_seq[-1] != 1:
        hailstone_seq.append(f(hailstone_seq[-1]))
    return hailstone_seq
#Problems
print("Problem 1")
print("The hailstone sequence for 1 = " + str(hailstone(1)))
print("Problem 2")
print("The hailstone sequence for 1 = " + str(hailstone(27)))
print("Problem 3")
longestseq = []
for n in range(1, 20000):
    curentseq = hailstone(n)
    if len(curentseq) > len(longestseq):
        longestseq = curentseq
print("The postitive integer <= 20000 is: " + str(longestseq[0]))
print("The lenght of the longest hailstone sequence with n <= 20000 is: " + str(len(longestseq)))
