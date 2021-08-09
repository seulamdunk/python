"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

#(0) 인자도 없고 리턴값도 없는 함수
'''
def func():
    print('inside func')

func()
result = func() # None > 리턴값이 없기때문에
print(result)



#(1) 리턴값이 여러개인 함수
def func(arg):
    return arg*2, arg+10
result = func(10)
print(result) # 튜플형식으로 리턴
print(result[0], result[1])

a,b = func(5) #리턴값을 unpacking
print(a,b)



# ==== (2) 위치인자 (positional argument) ====
def func(greeting, name):
    print(greeting, '!!!!', name + '님')

func('안녕', '홍길동')
func('길동', '헬로우')



# ==== (3) 키워드 인자 (keyword argument) ====
def func(greeting, name):
    print(greeting, '!!!!', name + '님')

func(greeting='안녕', name='홍길동')
func(name='길동', greeting='헬로우')


print()
# ==== (4) 인자(매개변수)의 기본값 지정하기 =====
def func(greeting, name='아무개'):
    print(greeting, '!!!!', name + '님')

# func('안녕','홍길동','서울') 인자 갯수가 맞지않으면 에러발생
func('안녕') # 기본값을 지정해주면 에러가 안남
func('안녕','스미스')

def func(a,b,c=100):
    return a*2 + b*3 +c*4

print(func(1,2))
print(func(1,2,3))
print(func(c=1,b=2,a=3))
'''




'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*)

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''

def func(a,b,c=0,*args):
    sum = a+b+c
    # print('*args:',args)
    for i in args:
        sum += i
    return sum

print(func(4,5))
print(func(4,5,6))
print(func(4,5,6,7))
print(func(4,5,6,7,8,9))



#(6) 키워드 인자 모으기 (**)
'''
    *args : positional argument 만 받을때
    **kwargs : keyword argument 받을때
'''
def func(a,b,c=0, *args, **kwargs):
    sum = a+b+c
    # print('*args:',args)
    for i in args: # args는 튜플
        sum += i
    # print(("kwargs:",kwargs)) # kwargs > 딕셔너리
    a =  for a in kwargs :


    return sum

print(func(4,5))
print(func(4,5,6))
print(func(4,5,6,7))
print(func(4,5,6,7,8,9))
print(func(4,5,6, kor=10, eng=20, math=30))
print(func(4,5,6,7,8, kor=10, eng=20))




