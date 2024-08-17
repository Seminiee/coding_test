'''
# BOJ 1926번 그림
1. 상하좌우로 연결된 그림의 크기를 알아내기
- pop()을 몇번하는지만 알면 ok
2. 도화지에 있는 모든 그림을 찾아내기
- 이중 for문을 돌면서 BFS의 시작점이 될 수 있는 곳을 찾으면 해결할 수 있음

'''

import sys
from collections import deque

col,row = map(int,sys.stdin.readline().split())
visit = [[0 for r in range(row)] for c in range(col)]

mat = list()
for c in range(col):
    mat.append(list(map(int,sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

drawing = list()

for c in range(col):
    for r in range(row):
        if mat[c][r] == 0 or visit[c][r]:
            continue
        visit[c][r] = 1
        queue = deque()
        queue.append((c,r))
        area = 0
        while(len(queue) != 0):
            area+=1
            y,x = queue.popleft()
            for pointer in range(4):
                nx = x + dx[pointer]
                ny = y + dy[pointer]
                if nx < 0 or nx >= row or ny <0 or ny >= col:
                    continue
                if visit[ny][nx] or not mat[ny][nx]:
                    continue
                
                visit[ny][nx] = 1
                queue.append((ny,nx))
        drawing.append(area)
print(len(drawing))
if len(drawing) == 0:
    max_drawing = 0
else:
    max_drawing = max(drawing)
print(max_drawing)

'''
while(not queue):
    y,x = queue.popleft()
    cnt += 1
    for pointer in range(4):
        nx = x + dx[pointer]
        ny = y + dy[pointer]
        if nx < 0 or nx >= row or ny <0 or ny >= col:
            continue
        if visit[ny][nx] or not mat[ny][nx]:
            continue
        
        visit[ny][nx] = 1
        queue.append((ny,nx))'''
#drawing.append(cnt)
