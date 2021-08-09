"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1,7):
    alist.append(n)
print(alist)

alist = list(range(1,7))
print(alist)


print()
#------------------------------------------------
# 리스트 컨프리핸션
blist = [n*2 for n in range(1,7)]
print(blist)

clist = [n*2 for n in range(1,7) if n%2 == 0]
print(clist)

dlist = []
for r in range(1,4) :
    for c in range(1,3):
        dlist.append((r,c))
print(dlist)

# 위의 일반 코딩을 파이썬답게 커프리핸션으로 변경하여 한 줄로 만들기
elist = [(n,m) for n in range(1,4) for m in range(1,3)]
print(elist)



print()
#-------------------------------------------
# 딕셔러니 컨프리핸션
datas = (2,3,4)
adic = {x: x**2 for x in datas}
print(adic)

word = 'LOVE LOL'
wcnt = { letter : word.count(letter) for letter in set(word)} # set > 중복을 막아줌
print(wcnt)



print()
#------------------------------------------------
# 셋 컨프리핸션
data = (1,2,3,1,2,4,5)
alist = [n for n in data]
print(alist)

alist = {n for n in data}
print(alist)




print()
# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
data = (1,2,3,2,1,4,5)
clist = (n for n in data)
print(clist)
print(list(clist))
print(list(clist))
















# -------------------------------------------------
# 프로젝트할 때 팀구호
우리의결의= """취하고싶으면달려라
맡은업무는반드시마치자
노력없는성과는없다
구글신과함께공부하자
"""
result = [ j[i*2] for i, j in enumerate(우리의결의.splitlines())]
print(result)