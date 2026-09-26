def fac(a):
    fact = 1
    for i in range(1, a+1):
        fact = fact*i
    return fact


n = fac(3)
print(n)
