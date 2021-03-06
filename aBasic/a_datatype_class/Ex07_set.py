# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다
#       - { }

s = set()               # 빈 집합을 생성
s = {}

s = set([1,2,3,1,1])
print(s)
s = {1,2,3,1,1}
print(s)
# print(s[0]) > set은 순서를 정하지 않기때문에 에러남

print('-------------------------------------')
s = {1,2,3,1,1}
s3 = {3,4,5,6}

#교집합
print(s & s3)
print(s.intersection(s3))

#합집합
print(s | s3)
print(s.union(s3))

#차집합
print(s - s3)

