print("Problem 1")
for n in range(20):
    print((n+1)**2)
print("Problem 2")
for n in range(20):
    print(((n+1)**2)%10)
print("Problem 3")
print("The last didget of a perfect square can never be 2,3,7,or 8")
print("Problem 4")
conjectured_set = [2,3,7,8]
print("begining Verification")
for n in range(10000):
    if (((n+1)**2)%10) in conjectured_set:
        print("Conjecture is false!")
print("Conjecture holds for 0 <= n <= 10000")
