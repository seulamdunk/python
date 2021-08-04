
print('1 ---------------------------------------------------')

a=[0,1,2,3,4]
print(a[:3], a[:-3])
# 0,1,2 , 0,1

print('2 ---------------------------------------------------')

a=[0,1,2,3,4]
print(a[::-1])
# 처음부터 끝까지 -1만큼 추출 > 역순으로 추출

print('3 ---------------------------------------------------')


first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
# order = [["egg", "salad", "bread", "soup", "canafe"], ["fish", "lamb", "pork", "beef", "chicken"], ["apple", "banana", "orange", "grape", "mango"]]
john = [order[0][:-2], second[1::3], third[0]]
# order[0][:-2] > "egg", "salad", "bread"
# second[1::3] > "lamb", "chicken"
# third[0] > "apple"
# john [["egg", "salad", "bread"], ["lamb", "chicken"], "apple"]

del john[2]
# john = [["egg", "salad", "bread"], ["lamb", "chicken"]]

john.extend([order[2][0:1]])
# extend() 리스트에 리스트를 더하기\
#[["egg", "salad", "bread"], ["lamb", "chicken"]],["apple", "banana"]

print(john)
#[["egg", "salad", "bread"], ["lamb", "chicken"]],["apple"]]


print('4 ---------------------------------------------------')

list_a = [3, 2, 1, 4]
list_b = list_a.sort()
# sort() 리스트 정렬
# [1,2,3,4]
print(list_a, list_b)
# [3,2,1,4], [1,2,3,4]


print('5 ---------------------------------------------------')

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])
# ['orange', 'strawberry', 'melon'], ['banana','orange']


print('6 ---------------------------------------------------')
num = [1, 2, 3, 4]
print(num * 2)
# [1,2,3,4,1,2,3,4]


print('6 ---------------------------------------------------')
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']

a.append('g')
# [1,2,3,5,g]
b.append(6)
# ['a', 'b', 'c','d','e', 6]

print('g' in b, len(b))
# Fasle, 6



print('6 ---------------------------------------------------')
list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']

list_b=[ ]

for i in range(len(list_a)): # for 변수 in range (횟수)

    if i % 2 != 1:
        list_b.append(list_a[i]) # 반복할 코드

print(list_b)
# ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']



print('7 ------------------------------------------------------')
a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')

b.append(6)

print('g' in b, len(b))
