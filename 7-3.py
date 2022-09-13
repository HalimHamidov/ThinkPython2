import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result



def estimate_pi():
    k = 0
    total = 0
    factor = 2*math.sqrt(2) / 9801
    
    while True:
        num = factorial(4*k)*(1103+26390*k)
        den = (factorial(k) ** 4) * (396 ** (4*k))
        term = num / den
        total = total + term * factor
        if abs(term) < 1e-15:
            break
        k = k + 1

    return (1 / total)

print("este_pi is", estimate_pi())
print("real_pi is",math.pi)
