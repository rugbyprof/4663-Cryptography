# Cryptomath Module

def succesiveSquaring(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = succesiveSquaring(base, exp // 2, mod)  # just / in Python 2
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod

def gcdr(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    k=0
    while a != 0:
        q = b // a
        r = b % a
        d = b
        a, b = b % a, a
        if k > 0:
            print('{} = {} x {} + {}'.format(d,q,b,r))
        k+=1
    return b


# Extended Euclidean algorithm 
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd_r(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        
# Extended Euclidean algorithm 
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd_i(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# GCD
#   returns the greatest common denominator. Thats it.
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# Mod Inverse V1
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
def modinv(a, m):
    g, x, y = egcd_r(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
        
# Mod Inverse V2
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# Euler's totient function
#   returns some integer that represents the positive integers 
#   less than or equal to n that are relatively prime to n.
def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            #print(k)
            amount += 1

    return amount

def SieveOfEratosthenes(n): 
    pass

if __name__ == '__main__':
    print(findModInverse(1051,17))
    print(succesiveSquaring(2,1234,789))


