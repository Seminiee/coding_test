import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())

'''
#: 벽
.: 지나갈 수 있는 공간
J: 지훈이의 미로에서의 초기 위치
F: 불이 난 공간

목표: 지훈이가 탈출하기 까지 시간이 얼마나 걸리나?
조건)
1. 미로의 가장 자리에 접한 공간에서 탈출할 수 있다.
2. 불은 각 지점에서 네 방향으로 확산된다.

로직)
1. 시작 지점부터 지나갈 수 있는 공간의 모든 거리를 계산한다.
2. 불의 시작지점부터 지나갈 수 있는 공간의 모든 거리를 계산한다.
3. 가장자리 중 지나갈 수 있는 공간의 거리를 비교한다
    3-1. 1번 DFS의 결과가 작으면 탈출 가능하고, 최솟값+1이 정답
    3-2. 2번 DFS의 결과가 같거나 크면 탈출 불가능하여 IMPOSSIBLE
'''
maze = list()
dist = [[0 for r in range(row)] for c in range(col)]
dist_fire = [[0 for r in range(row)] for c in range(col)]
for c in range(col):
    maze.append(list(sys.stdin.readline().rstrip()))

queue_run = deque()
queue_fire = deque()
check_list = list()

for c in range(col):
    for r in range(row):
        if maze[c][r] == 'J':
            dist[c][r] = 1
            start = (c,r)
            queue_run.append(start)
        elif maze[c][r] == 'F':
            queue_fire.append((c,r))
            dist_fire[c][r] = 1
        elif maze[c][r] == '.':
            dist[c][r] = -1
        if maze[c][r] not in '#F' and (c == 0 or r == 0 or r == (row-1) or c == (col-1)):
            check_list.append((c,r))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while(len(queue_fire) != 0):
    y2,x2 = queue_fire.popleft()
    for cursor in range(4):
        nx = x2 + dx[cursor]
        ny = y2 + dy[cursor]
        if nx <0 or nx >= row or ny <0 or ny >= col:
            continue
        if maze[ny][nx] == '#': # 벽
            continue
        if dist_fire[ny][nx] > 0: # 벽이 아니고 이미 방문한 곳
            continue
        dist_fire[ny][nx] = dist_fire[y2][x2] + 1
        queue_fire.append((ny,nx))

while(len(queue_run) != 0):
    y1,x1 = queue_run.popleft()
    for cursor in range(4):
        nx = x1 + dx[cursor]
        ny = y1 + dy[cursor]
        if nx < 0 or nx >= row or ny < 0 or ny >= col:
            continue
        if maze[ny][nx] == '#': #벽
            continue
        if dist[ny][nx] > 0: # 갈 수 있는 공간인데 방문함
            continue
        if dist[y1][x1] + 1 >= dist_fire[ny][nx] and dist_fire[ny][nx] > 0:
            continue
        dist[ny][nx] = dist[y1][x1] + 1
        queue_run.append((ny,nx))

t = list()
for y,x in check_list:
    if (dist[y][x] > 0 and dist[y][x] < dist_fire[y][x]) or dist[y][x] > 0 and dist_fire[y][x] == 0:
        t.append(dist[y][x])
if start in check_list:
    t.append(1)
if len(t) == 0:
    print("IMPOSSIBLE")
else:
    print(min(t))