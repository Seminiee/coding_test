#%%
import heapq
import sys
#%%
num_amount = int(sys.stdin.readline())

arr = list()
heapq.heapify(arr)

for i in range(num_amount):
    num = int(input())
    if num:
        heapq.heappush(arr,num)
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr))
    
#%%
from collections import deque

num_amount = int(sys.stdin.readline())
arr = list()

for i in range(num_amount):
    num = int(sys.stdin.readline())
    arr.sort()
    queue = deque(arr)
    if num:
        queue.append(num)
    else:
        if len(queue) == 0:
            print(0)
        else:
            print(queue.popleft())
    arr = list(queue)

#%%
num_amount = int(sys.stdin.readline())
arr = list()

pointer = 0
for i in range(num_amount):
    num = int(input())
    arr.sort()
    if num:
        arr.append(num)
    else:
        if pointer == len(arr):
            print(0)
        else:
            print(arr[pointer])
            pointer+=1

#print(num_amount)
# %%
