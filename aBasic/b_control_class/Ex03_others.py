msg = '행복해'            # 문자열
li = ['a','b','c']       # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = {'k': 5, 'j': 6, 'l':7 }    # 딕셔너리

# (1) unpacking : 각 요소를 분해(풀기) ======================
a, b, c = msg
# 변수의 갯수와 요소의 갯수(글자수?)가 맞으면 알아서 들어감
# a,b,c = 행,복,해
print(a)
print(b)
print(c)

print()
a, b, c = li
print(a)
print(b)
print(c)

print()
a, b, c = di.items() # .iems()를 붙여줘야 밸류값도 같이 들어감
print(a)
print(b)
print(c)


print("-------------------------------------------------")
# (2) 리스트의 요소로 튜플인 경우의 예 ======================
# for문과 unpacking 이용하여 튜플의 요소끼리 더한 값을 출력
alist = [(1,2), (3,4), (5,6)]

for a,b in alist:
    print(a + b)



print("-------------------------------------------------")
# (3) enumerate() : 인덱스와 같이 추출하고자 ======================
user_list = ['개발자', '코더', '전문가', '분석가']

for user in enumerate(user_list):
    print(user)

# unpacking + enumarate를 이용하여 인덱스와 요소를 따로 추출
for idx, user in enumerate(user_list):
    print(idx, '번째', user)




print("-------------------------------------------------")
# (4) zip() : 리스트의 요소를 인덱스별로 묶어준다 ******
days = ['월', '화', '수']
doit = ['잠자기', '공부', '놀기', '밥먹기']
mons = [5,6,7]

print(list(zip(days,doit,mons)))
# days와 doit를 zip으로 묶는다  >  zip를 list로 푼다

print(dict(zip(days,doit))) # mons
# dictionary는 key-value로 잡기때문에 3개이상은 안된다