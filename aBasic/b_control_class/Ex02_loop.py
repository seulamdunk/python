
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

for entry in e: # a는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)

for entry in e.items():
    print('key=', entry[0], 'value=', entry[1])

for key, val in e.items():
    print('key=', key, 'value=', val)


print('=================================')
# 1~10까지 합 구하기
sum=0
for i in range(1,11):
    sum += i
print('1부터 10까지의 합:',sum)
print(i)


print('=================================')
# 1~10까지 홀수합 구하기
sum=0
for i in range(1,11):
    if i%2 == 1:
        sum += i
print('1부터 10까지 홀수의 합:', sum)
print('=================================')
# 1~10까지 홀수합 구하기
sum=0
for i in range(1,11,2):
    sum += i
print('1부터 10까지 홀수의 합:', sum)


"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2,10):
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))

print('=================================')
#while
a=['x','y','z']

while a: # 집합요소에 빈 요소인 경우만 False, 요소가 하나라도 있으면 True
    data = a.pop()
    print(data)
    if data == 'y':
        break # while문 종료
    print(a)
else:
    print(a)
    print('end')
