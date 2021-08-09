
'''
pin =  '880122-1234567'
birthday = '홍길동님 생년월일 : ' + '880122'

pin.split('-')
gender = int(pin.split('-')[1][0])
if gender == 1:
    gender = '성별 : 남자'
else:
    gender = '성별 : 여자'

print(birthday)
print(gender)



a=[1,3,5,4,2]
a.sort(reverse=True)
print(a)





a = ['독도는', '대한민국의', '아름다운', '섬입니다']
result = ' '.join(a)
print(result)





a=(1,2,3)
a = a + '4'
print(a)



a = b = [1,2,3]
a[1] = 4
print(b)



#6
i=1
while i < 6:
    print('*' * i)
    i += 1



#7
import statistics

kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]

kor_score = statistics.mean(kor_score)
math_score = statistics.mean(math_score)
eng_score = statistics.mean(eng_score)

midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)


keys = ['animal', 'plants','other']
life = dict.fromkeys(keys)
keys2 = ['cats', 'octopi', 'emus']
life = dict.fromkeys(keys2, keys[0])
print(life)

import statistics

kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50,60,70,80,90]

sum_kor_score = sum(kor_score)
sum_math_score = sum(math_score)
sum_eng_score = sum(eng_score)

avg_kor_score = sum_kor_score/len(kor_score)
avg_math_score = sum_math_score/len(math_score)
avg_eng_score = sum_eng_score/len(eng_score)

kor_score = (sum_kor_score, avg_kor_score)
math_score = (sum_math_score, avg_math_score)
eng_score = (sum_eng_score, avg_eng_score)

midterm_score = [kor_score, math_score, eng_score]


'''

life = {
    'animal' : {
        'cats' : ['kim', 'lee', 'choi'],
        'octopi' : {},
        'emus' : {}
    },
    'plants' : {},
    'other' : {}
}


