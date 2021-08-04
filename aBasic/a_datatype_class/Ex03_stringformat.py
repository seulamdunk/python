
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#               자바의 +대신 파이썬에서는 ,로 연결
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#               c나 자바에서 printf() 유사
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴


# format()이용
print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
print('내가 좋아하는 숫자는 %d 이다' % 100 )
print()

msg = '{}님 오늘도 행복합시다'
print(msg.format('홍길동'))
print('{}님 오늘도 행복합시다'.format('홍길동'))
print()

msg = '{}님 오늘도 행복합시다 - {}로부터'
print(msg.format('홍길동', '개발팀'))

msg = '{0}님 오늘도 행복합시다 - {1}로부터'
print(msg.format('홍길동', '개발팀'))

msg = '{1}님 오늘도 행복합시다 - {0}로부터'
print(msg.format('홍길동', '개발팀'))

msg = '{name}님 오늘도 행복합시다 - {team}로부터'
print(msg.format(name='홍길동', team='개발팀'))

print()

# [참고] http://pyformat.info

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456

print('%s님은 %d세 이고 신장은 %f cm입니다' % (name, age, height) )
print('%s님은 %d세 이고 신장은 %10.3f cm입니다' % (name, age, height) )
print()
print('%s님은 %d세 이고 신장은 %.1f cm입니다' % (name, age, height) )
#위의 출력문과 동일하게 format() 이용하여 출력
msg='{0}님은 {1}세 이고 신장은 {2:.1f} cm입니다'
print(msg.format(name, age, height))




#--------------------------------------------------
# 실수인 경우


