import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
complex = list()

for i in range(N):
    complex.append(list(map(int, sys.stdin.readline().rstrip())))

visit = [[0 for r in range(N)] for c in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

complex_list = list()

for c in range(N):
    for r in range(N):
        if complex[c][r] == 0 or visit[c][r]:
            continue
        local = 0
        visit[c][r] = 1
        queue = deque()

        queue.append((c,r))
        while(len(queue) != 0):
            local+=1
            y,x = queue.popleft()
            for cursor in range(4):
                nx = x + dx[cursor]
                ny = y + dy[cursor]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if complex[ny][nx] == 0 or visit[ny][nx]:
                    continue
                visit[ny][nx] = 1
                queue.append((ny,nx))
        complex_list.append(local)
complex_list.sort()
ans1 = len(complex_list)
if ans1:
    print(ans1)
    for i in range(len(complex_list)):
        print(complex_list[i])
else:
    print(ans1)