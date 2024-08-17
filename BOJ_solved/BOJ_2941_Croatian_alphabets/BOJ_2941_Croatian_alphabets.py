'''
#2941 크로아티아 알파벳

전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

  크로아티아 알파벳	    변경
                č	    c=
                ć	    c-
                dž	    dz=
                đ	    d-
                lj	    lj
                nj	    nj
                š	    s=
                ž	    z=
예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

*입력
첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

*출력
입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
'''

txt = input()

alpha_list = list()

for i in range(len(txt)):
    t = txt[i]
    if t == '=':
        if i < 2:
            p1 = txt[i-1]
            if p1 in ['c','s','z']:
                tmp = p1 + t
                alpha_list.remove(p1)
        else:
            p1 = txt[i-1]
            p2 = txt[i-2]
            if p2 == 'd' and p1 == 'z':
                tmp = p2+p1+t
                alpha_list.remove(p2)
                alpha_list.remove(p1)
            else:
                if p1 in ['c','s','z']:
                    tmp = p1 + t
                    alpha_list.remove(p1)
    elif t == 'j':
        p1 = txt[i-1]
        if p1 in ['l','n']:
            tmp = p1 + t
            alpha_list.remove(p1)
        else:
            tmp = t
    elif t == '-':
        p1 = txt[i-1]
        tmp = p1 + t
        alpha_list.remove(p1)
    else:
        tmp = t
    alpha_list.append(tmp)

#print(alpha_list)
print(len(alpha_list))