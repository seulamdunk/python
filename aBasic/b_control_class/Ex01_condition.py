"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록{}을 대신 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

a = -1
if a:
    print('True') #
else:
    print('False')

print('======')

a = 10
b = -1

print(a and b) #-1
print(a or b) #10

'''
    A B     A & B       A | B
    --------------------------
    T T       T           T
    T F       F           T
    F T       F           T
    F F       F           F
'''
if a and b:
    print('True') #
else:
    print('False')

if a or b:
    print('True') #
else:
    print('False')

print('======')
a = 10
if a:
    c=2
elif b:
    c=4
else :
    c=6

print(c) # 2


print('======')
#------------------------------------
word = 'korea'

if word.find('k')>-1: # korea에 'k'포함하면 출력
    print('1 > '+word)
# find 인덱스를 검색 > k의 인덱스 0 > 0은 False이기 때문에 출력되지 않음

if word.find('z')>-1:  # korea에 'z'포함하면 출력
    print('2 > '+word)
# find 인덱스를 검색 > z의 인덱스 없음  > 0이 아닌 숫자는 True이기 때문에 출력
# 제대로 출력되려면 -1보다 크다라는 조건을 걸어준다






