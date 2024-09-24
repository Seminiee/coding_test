import sys
T = int(sys.stdin.readline().rstrip())

base_list = [0,1,2,4]
n_list = list()
for i in range(T):
    n_list.append(int(sys.stdin.readline().rstrip()))

m = max(n_list)
for i in range(4,m+1):
    t = base_list[i-1] + base_list[i-2] + base_list[i-3]
    base_list.append(t)

for k in n_list:
    print(base_list[k])
'''
3
1 1 1 
1 2
2 1
3

4
1 1 1 1
1 2 1
2 1 1
3 1     arr[4-1]

1 1 2   arr[4-2]
2 2

1 3     arr[4-3]





5
1 1 1 1 1
1 2 1 1
2 1 1 1
3 1 1
1 1 2 1
2 2 1
1 3 1     arr[5-1]

1 1 1 2
1 2 2
2 1 2
3 2     arr[5-2]

2 3
1 1 3 arr[5-3]
'''

