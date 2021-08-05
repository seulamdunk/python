
'''
print('1=====================')

num1 = int(input('정수를 입력하세요:'))
num2 = int(input('정수를 입력하세요:'))
num3 = int(input('정수를 입력하세요:'))
num4 = int(input('정수를 입력하세요:'))
num5 = int(input('정수를 입력하세요:'))
avg = (num1 + num2 + num3 + num4 + num5)/5
print('평균=', avg)




print('2=====================')
text = input('문자열입력:')
result = text[::-1]
print('결과:', result)
'''
import math

print('3=====================')
numlist = list(map(int, input('정수리스트 입력:').split()))
avg = sum(numlist) / len(numlist)
print('평균=', avg)

vsum = 0
for i in numlist:
    vsum += (i - avg) ** 2
var = vsum / len(numlist)
std = math.sqrt(var)
print('표준편차= ', round(std,2))