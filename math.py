

def _gcd(a, b):
    if(a < b):
        a, b = b, a
    r = a % b    
    if r == 0:
        return b
    else:
        return _gcd(b, r)

def _lcm(a,b):
    return (a * b)/_gcd(a,b)

# returns the base b expansion of n
# where n has a base of 10
def _base_expansion(n, b):
    _remainders = []
    q, r = divmod(n,b)

    while q > 0:
        _remainders = [r] + _remainders
        q, r = divmod(q, b)
        if q == 0:
            _remainders = [r] + _remainders
    return int("".join(str(x) for x in _remainders))

