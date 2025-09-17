n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

result = []

for i in range(n - 7):
    for j in range(m - 7):
        w_cnt = 0  # 좌상단 W로 시작하는 경우
        b_cnt = 0  # 좌상단 B로 시작하는 경우
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if chess[i + x][j + y] != 'W': w_cnt += 1
                    if chess[i + x][j + y] != 'B': b_cnt += 1
                else:
                    if chess[i + x][j + y] != 'B': w_cnt += 1
                    if chess[i + x][j + y] != 'W': b_cnt += 1
        result.append(min(w_cnt, b_cnt))

print(min(result))