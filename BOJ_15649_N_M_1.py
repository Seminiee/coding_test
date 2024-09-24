import sys
n,m = map(int, sys.stdin.readline().split()) # 1이상 n이하 자연수로 m개를 순열, 사전 순 배열

lis = [0 for x in range(10)]

#num_list = [x for x in range(1,n+1)]
visited = [False for x in range(10)]

def backtracking(k):
    if k == m:
        for i in range(m):
            print(lis[i],end=' ')
        print()
        return
    for i in range(1,n+1):
        if visited[i] == False:
            lis[k] = i
            visited[i] = True
            backtracking(k+1)
            visited[i] = False
            
backtracking(0)       


'''
def backtracking(x):
	if 정답이라면:
		정답 출력
		return
	else: (정답이 아니라면)
		for 뻗을 수 있는 모든 자식 노드에 대해서:
			if 정답에 유망한 노드라면(Promising Node):
				자식노드로 이동
				backtracking(x+1)
				부모 노드로 이동 (return 후에 여기가 실행 됨)
'''