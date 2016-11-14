

def _gcd(a, b):
    """Returns the greatest common divisor
       of two numbers.

        Params:
            a (int)
            b (int)
    """
    a = abs(a)
    b = abs(b)

    if(a < b):
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    else:
        return _gcd(b, r)


def _lcm(a, b):
    """Returns the lowest common multiple
       of two numbers.

        Params:
            a (int)
            b (int)
    """
    return abs((a * b)/_gcd(a, b))


def _base_expansion(n, b):
    """Returns the base b expansion of
       a base ten number n.

        Params:
            n (int): Base ten number
            b (int): Base expansion
    """
    _remainders = []
    q, r = divmod(n, b)
    
    if q == 0:
        _remainders.append(r)

    while q > 0:
        _remainders = [r] + _remainders
        q, r = divmod(q, b)
        if q == 0:
            _remainders = [r] + _remainders

    return int("".join(str(x) for x in _remainders))


def _base_ten(n, b):
    """Returns n as a base 10 number.

        Params:
            n (int)
            b (int): Base of n
    """
    n = str(n)
    k = 0

    for i in n:
        i = int(i)
        k = b * k + i

    return(k)


# TODO: identical objects
def _permutation(n, r, repetition=False):
    """Return the number of permutations.

        Params:
            n (int): Number of objects in a set
            r (int): Number of objects being chosen
            repetition (boolean): Specifies if repeats are allowed
    """
    if repetition is True:
        return n**r

    permutation = 1
    for i in range(r):
        permutation *= n - i

    return permutation


def _combination(n, r, repetition=False):
    """Return the number of combinations.

        Params:
            n (int): Number of objects in a set
            r (int): Number of objects being chosen
            repetition (boolean): Specifies if repeats are allowed
    """

    numerator = 1
    denominator = 1

    if repetition is True:
        c = n - 1
        p = r + c

        for i in range(p):
            numerator *= p - i
            if i < r:
                denominator *= r - i
            if i < c:
                denominator *= c - i

    else:
        for i in range(r):
            numerator *= n - i
            denominator *= r - i

    return numerator // denominator
