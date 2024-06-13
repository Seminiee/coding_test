import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())
dist = [[-1 for r in range(row)] for c in range(col)]

maze = list()

for c in range(col):
    maze.append(list(map(int,sys.stdin.readline().rstrip())))
dist[0][0] = 0
#print(maze)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append((0,0))

while(len(queue) != 0):
    y,x = queue.popleft()
    for cursor in range(4):
        nx = x + dx[cursor]
        ny = y + dy[cursor]
        if nx <0 or nx >= row or ny < 0 or ny >= col:
            continue

        if dist[ny][nx] >= 0 or maze[ny][nx] != 1:
            continue

        dist[ny][nx] = dist[y][x] + 1
        queue.append((ny,nx))

answer = dist[col-1][row-1]
print(answer+1)