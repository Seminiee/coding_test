# input(): 한 줄을 읽어옴(구분문자 없음, 문자열로 읽어옴)
## 1. 파일로 입력 받기
import sys
sys.stdin = open("input.txt","r")

## 2. 한 줄을 읽어서 정수로 변환
N = int(input())

## 3. 한 줄을 읽고 공백으로 구분된 문자를 입력받기
print(input().split())

## 4. 한 줄을 읽고 **공백으로 구분된** 문자를 정수로 변환
### 4-1) 정수의 개수를 알 때
N,M = map(int,input().split())

### 4-2) 정수의 개수를 모를 때 -> 리스트로 묶어서 받는다
arr = list(map(int,input().split()))

## 5. 이어진 문자/숫자를 한자리씩 나눠서 리스트에 저장: _문자열 리스트_로 저장
arr = list(input())

## 6. 이어진 숫자를 한자리씩 나눠서 리스트에 저장: _숫자형 리스트_로 저장
arr = list(map(int,input()))

# sys.stdin.readlin() -> input() 보다 훨씬 빠르다
##주의점)
## sys.stdin.readline()은 한 줄 단위로 입력받기 때문에, 개행문자(\n)가 같이 입력받아짐 ex) 3을 입력했다면 3\n이 저장됨.
## 변수 타입이 문자열 형태(str)로 저장됨

## 1. 한 개의 정수를 입력받을 때
import sys
a = int(sys.stdin.readline())

## 2. 정해진 개수의 정수를 한 줄에 입력받을 때
import sys
a,b,c = map(int, sys.stdin.readline().split())

## 3. 임의의 개수의 정수를 한 줄에 입력받아 리스트에 저장할 때
import sys
data = list(map(int, sys.stdin.readline().split()))

## 4. 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때

import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

## 5. 문자열 n줄을 입력받아 리스트에 저장할 때
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
