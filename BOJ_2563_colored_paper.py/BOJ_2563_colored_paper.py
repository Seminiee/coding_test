'''
#2563 색종이

문제
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

*입력
첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 
색종이를 붙인 위치는 두 개의 자연수로 주어지는데 
첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 
두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 
색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

*출력
첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.
'''
count = int(input())

colored_paper = list()
for i in range(count):
    x,y = map(int,input().split(' '))
    colored_paper.append((x,y))

colored_paper.sort(key=lambda x:(x[0],x[1]))

'''
count = int(input())

if count == 0:
    print(0)
elif count == 1:
    print(100)
else:
    colored_paper = list()

    max_x = 0

    for i in range(count):
        x,y = map(int,input().split(' '))
        if x > max_x:
            max_x = x
        colored_paper.append((x,y))

    colored_paper.sort(key=lambda x:(x[0],x[1]))

    sum = 0
    for cur_x in range(0,max_x+10):
        overlap_set = set()
        for k in range(count):
            x,y = colored_paper[k]
            if cur_x < x:
                break
            if cur_x >= (x+10):
                continue
            overlap_set.add(y)
        overlap = list(overlap_set)

        overlap.sort()
        if len(overlap) == 0:
            continue
        elif len(overlap) == 1:
            sum += 10
            continue
        else: 
            y_len = 0
            for i in range(len(overlap)-1):
                y = overlap[i]
                y_next = overlap[i+1]
                if (y_next - y) >= 10:
                    y_len+=10
                else:
                    y_len += (y_next - y)
                sum += (y_len+10)   
    print(sum)
'''
'''
overlap = 0
for i in range(count-1):
    #print('i: ',i)
    x1,y1 = colored_paper[i]
    for j in range(i+1,count):
        #print('j: ',j)
        x2,y2 = colored_paper[j]
        abs_x = abs(x1-x2)
        abs_y = abs(y1-y2)
        if (abs_x>=10):
            continue
        elif (abs_y >= 10):
            continue
        else:
            overlap_x = (10-abs_x)
            overlap_y = (10-abs_y)
            cur_overlap = overlap_x * overlap_y
            overlap+=cur_overlap
            #print('cur_overlap: ', cur_overlap)
#print(overlap)
print(100*count - overlap)
'''