'''
#1157 단어 공부

문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

*입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

*출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

word = input()
word = word.lower()

alphabets = ['a','b','c','d','e',
             'f','g','h','i','j',
             'k','l','m','n','o',
             'p','q','r','s','t',
             'u','v','w','x','y','z']
a_c = [0 for x in range(len(alphabets))]

for i in word:
    for j in range(len(alphabets)):
        if i == alphabets[j]:
            a_c[j]+=1
            break
ind = a_c.index(max(a_c))
ans=alphabets[ind].upper()
for i in range(len(a_c)):
    if i == ind:
        continue
    if a_c[i] == a_c[ind]:
        ans = '?'
        break
print(ans)


'''
word = input()
word = word.lower()

a_set = set(word)
a_list = list(a_set)

c = [0 for x in range(len(a_list))]

for i in range(len(word)):
    for j in range(len(a_list)):
        if word[i] == a_list[j]:
            c[j]+=1
            break

if len(set(c)) < len(a_list):
    print('?')
else:
    ind = c.index(max(c))
    print(a_list[ind].upper())
'''