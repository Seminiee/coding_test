import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())
depot = list()
dist = [[0 for r in range(row)] for c in range(col)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for c in range(col):
    depot.append(list(map(int,sys.stdin.readline().split())))

for c in range(col):
    for r in range(row):
        if depot[c][r] == 1:
            queue.append((c,r))
            dist[c][r] = 0
        elif depot[c][r] == 0:
            dist[c][r] = -1


while(len(queue) != 0):
    y,x = queue.popleft()
    for cursor in range(4):
        nx = x + dx[cursor]
        ny = y + dy[cursor]
        if nx < 0 or nx >= row or ny < 0 or ny >= col:
            continue
        if dist[ny][nx] >= 0:
            continue
        dist[ny][nx] = dist[y][x] + 1
        queue.append((ny,nx))

answer = 0 
for lis in dist:
    if -1 in lis:
        answer = -1
        break
    answer = max(answer, max(lis))
print(answer)