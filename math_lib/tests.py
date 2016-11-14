from algorithms.math_lib.math_lib import _gcd, _lcm
from algorithms.math_lib.math_lib import _base_expansion, _base_ten
from algorithms.math_lib.math_lib import _permutation, _combination


### GCD Tests ###
assert _gcd(34, 6) == 2
assert _gcd(360,39736) == 8
assert _gcd(-6, 34) == 2

### LCM Tests ###
assert _lcm(65, 10) == 130
assert _lcm(60, 3350) == 20100
assert _lcm(3350, -60) == 20100

### BaseExpansion Tests ###
assert _base_expansion(8, 2) == 1000
assert _base_expansion(2, 5) == 2
assert _base_expansion(16, 16) == 10

### BaseTen Tests ###
assert _base_ten(1000, 2) == 8
assert _base_ten(16, 16) == 22
assert _base_ten(2, 15) == 2


### Permutation Tests ###
assert _permutation(20, 3, repetition=False) == 6840
assert _permutation(20, 3, repetition=True) == 8000


### Combination Tests ###
assert _combination(20, 3, repetition=False) == 1140
assert _combination(20, 3, repetition=True) == 1540

