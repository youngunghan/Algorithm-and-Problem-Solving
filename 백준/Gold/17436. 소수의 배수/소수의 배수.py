import sys
import math
from itertools import combinations

input = sys.stdin.read
data = input().split()

# 입력 처리
N = int(data[0])
M = int(data[1])
primes = list(map(int, data[2:]))

def lcm(a, b):
    return a * b // math.gcd(a, b)

# 포함-배제 원리를 사용하여 해결
def count_divisible_by_primes(N, M, primes):
    total = 0
    num_primes = len(primes)
    
    # 모든 비트 마스크 생성 (1부터 2^N-1)
    for r in range(1, num_primes + 1):
        for comb in combinations(primes, r):
            # 현재 조합의 LCM 계산
            current_lcm = 1
            for prime in comb:
                current_lcm = lcm(current_lcm, prime)
                if current_lcm > M:
                    break
            
            # M 이하의 current_lcm의 배수 개수
            divisible_count = M // current_lcm
            
            # 조합의 원소 개수에 따라 더하거나 뺌
            if len(comb) % 2 == 1:  # 홀수인 경우
                total += divisible_count
            else:  # 짝수인 경우
                total -= divisible_count
    
    return total

# 결과 출력
print(count_divisible_by_primes(N, M, primes))