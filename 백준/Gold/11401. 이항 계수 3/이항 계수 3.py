import sys
input = sys.stdin.readline

MOD = 1000000007

def power(base, exp):
    """
    Calculate (base^exp) % MOD using fast exponentiation
    Time complexity: O(log exp)
    """
    res = 1
    while exp > 0:
        if exp & 1:
            res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
    return res

def binomial_coefficient(n, k):
    """
    Calculate C(n,k) % MOD using Fermat's Little Theorem
    Time complexity: O(min(k, n-k))
    
    Example:
    >>> binomial_coefficient(5, 2)
    10
    """
    num, den = 1, 1
    for i in range(k):
        num = num * (n - i) % MOD
        den = den * (i + 1) % MOD
    return num * power(den, MOD - 2) % MOD

n, k = map(int, input().split())
print(binomial_coefficient(n, k))