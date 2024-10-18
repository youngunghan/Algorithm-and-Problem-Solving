import sys

MOD = 1000000007

def catalan(n):
    if n % 2 == 1:
        return 0
    
    n //= 2
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD

    return dp[n]

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    print(catalan(L))