

def _gcd(a, b):
    if(a < b):
        a, b = b, a
    quotient, r = divmod(a,b)    
    if r == 0:
        return b
    else:
        return _gcd(b, r)

def _lcm(a,b):
    return (a * b)/_gcd(a,b)

