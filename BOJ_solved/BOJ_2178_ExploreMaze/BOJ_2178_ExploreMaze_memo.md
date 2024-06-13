### [BOJ 2178 미로탐색](https://www.acmicpc.net/problem/2178)
- BFS로 구현
    + dist 배열
        - -1로 초기화하여 방문여부 확인
        - `dist[0][0]`은 0으로 초기화한 다음 BFS
    + 개인적인 실수: `deque`로 queue구현 시 `popleft()`