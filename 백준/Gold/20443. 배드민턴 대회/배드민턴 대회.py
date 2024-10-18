import sys
input = sys.stdin.readline

MOD = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half = power(base, exponent // 2)
        return (half * half) % MOD
    else:
        return (base * power(base, exponent - 1)) % MOD

def derangement(n):
    result = 0
    for i in range(n + 1):
        term = factorial(n) * power(-1, i) * power(factorial(i), MOD - 2)
        result = (result + term) % MOD
    return result

N = int(input())

total = 0
for k in range(4):
    if (N - k) % 4 == 0:
        participants = N - k
        combinations = factorial(N) * power(factorial(k) * factorial(N - k), MOD - 2)
        total = (total + combinations * derangement(participants)) % MOD

print(total)