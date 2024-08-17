'''
#1463 <1로 만들기>
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

*입력
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.

*출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

def make_1(n):
    base_List = [0,0,1,1]
    if(n<=3):
        return base_List[n]
    for i in range(4,n+1):
        k=0
        if i % 3 == 0:
            k1 = 1 + base_List[i // 3]
            k2 = 1 + base_List[i // 2]
            if k1 >= k2:
                k = k2
            else:
                k = k1
        else:
            if i % 2 == 0:
                k1=0
                k2=0
                k1 = 1 + base_List[i // 2]
                k2 = 1 + base_List[i - 1]
                if k1 >= k2:
                    k = k2
                else:
                    k = k1
            else:
                k = 1 + base_List[i - 1]
        base_List.append(k)
    ret = base_List[n]
    return ret

input_n = int(input())
ans = make_1(input_n)

print(make_1(input_n))
