'''
input = 5

output)
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

N = int(input())
for i in range(1,2*N):
    if i <= N:
        t = i
    else:
        t = 2*N - i
    tmp = ""
    for k in range(N-t):
        tmp+=" "
    for k in range(2*t-1):
        tmp+="*"
    print(tmp)
'''
for i in range(1,2*N):
    if i <= N:
        t = i
    else:
        t = 2*N - i
    for k in range(5-t):
        print(" ",end="")
    for k in range(2*t-1):
        print("*",end="")
    if i == (2*N-1):
        print("",end="")
    else:
         print()
'''

