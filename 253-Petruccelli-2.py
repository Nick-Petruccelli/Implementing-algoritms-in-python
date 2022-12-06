print("Problem 1")
A = {0,1,2,3,5,10,12}
B = {2,4,6,8,10,12,14,16}
AuB = A|B
AnB = A&B
A_B = A-B
B_A = B-A
print("AuB = ",AuB)
print("AnB = ",AnB)
print("A-B = ",A_B)
print("B-A = ",B_A)
print("Problem 2")
E = set()
for n in range(1,51,1):
    E.add(n*2)
print("E =",E)
print("Problem 3")
F = set()
for n in range(1,101,1):
    if n%2 == 0%2:
        F.add(n)
print("F =",F)
print("Problem 4")
for n in E:
    if n not in F :
        print("Sets not equal")
        break
for n in F:
    if n not in E:
        print("Sets not equal")
        break
if E == F:
    print("Sets equal")
else:
    print("sets not equal")
