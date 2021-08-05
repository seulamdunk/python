"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
'''
name = input('이름입력:')
print('당신은 ' + name + '입니다')
print('당신은',name ,'입니다')
print('------------------------------------')
# format() 이용하여 동일하게 출력
# % 이용하여 동일하게 출력
print('당신은 {0}입니다'.format(name))
print('당신은 %s입니다' % name)
'''

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
# age = int(input('나이입력:'))
# print(age+1,'세')

# height = eval(input('키 입력:'))
# print(height,'cm')
# print(type(height))

print('1+2')
print(eval('1+2'))



#----------------------------------
# 단을 입력받아 구구단을 구하기
'''
dan = int(input('단 입력:'))
for i in range(1,10):
    print("{} * {} = {}".format(dan, i, dan*i))

'''



#-----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕', '친구')
print('안녕' '친구')

'''
for i in range(5):
    print(i)
print('=====')
for i in range(5):
    print(i, end=',' if i<3 else '')
'''




# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자

# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3
# 문자열을 받아 처리
import sys
args = sys.argv[1:]
for i in args:
    print(i)