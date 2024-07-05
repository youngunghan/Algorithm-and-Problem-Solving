import sys
input = sys.stdin.readline
N = int(input())
ns = list(map(int, input().split()))
ns.sort()
M = int(input())
ms = list(map(int, input().split()))
# for m in ms:
#     print(1 if m in ns else 0)

import bisect
for i in range(M):
    K = bisect.bisect_left(ns, ms[i])
    print(1) if K < N and ns[K] == ms[i] else print(0)