'''
#2738 행렬 덧셈

문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. 
N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
'''

m,n = map(int,input().split(' '))

mat1 = list()
mat2 = list()

for i in range(m):
    row = list(map(int,input().split()))
    mat1.append(row)

for i in range(m):
    row = list(map(int,input().split()))
    mat2.append(row)
mat3 = list()
for i in range(m):
    row = list()
    for j in range(n):
        t = mat1[i][j] + mat2[i][j]
        row.append(t)
    mat3.append(row)

for i in range(m):
    for j in range(n):
        print(mat3[i][j],end=' ')
    print()

