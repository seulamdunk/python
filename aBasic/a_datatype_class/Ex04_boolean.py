# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

# 논리형(부울형) 변수
hungry = True
sleep = False

print(type(hungry)) # class 'bool'
print(not hungry) # True
print(hungry and sleep) # False
print(hungry or sleep) # True
print(hungry & sleep) # False
print(hungry | sleep) # True




"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False


"""
print()
if('아'):
    print('True') #
else:
    print('False')

if([]):
    print('True2')
else:
    print('False2') #

if(0):
    print('True')
else:
    print('False') # 0은 fasle

if(-1):
    print('True2') # 0이 아닌 숫자는 true
else:
    print('False2')



