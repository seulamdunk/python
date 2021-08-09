


# 1
list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):
    a = set(list_data) # set() 중복을 제거 후 정렬 [0,1,3,4,5,7,8]
    return list(a)[1:5]
quiz_2(list_1)



#2
'''
(가) 나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조로, LIFO(Last In First Out)로 구현된다.
> 스택
(나) 먼저 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조로, FIFO(First In First Out)로 구현된다.
> 큐
(다) 값의 변경이 불가능하며, 리스트의 연산, 인덱싱, 슬라이싱 등을 동일하게 사용한다.
> 튜플
(라) 값을 순서 없이 저장하면서 중복을 불허한다.
> set
'''


#3
def delete_a_list_element(list_data, element_value):
    if element_value in list_data:
        list_data.remove(element_value)
        return list_data
    else:
        return "False"

list_data = ['a', 1, 'gachon', '2016.0'] # '2016.0' > 문자형
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)
# False


#4
a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)
print(b+c) # 2019



#5
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(data_1, data_2):
    result = []
    for i in (tuple_1 + tuple_2):
        result.append(i)
    return result

print(quiz_1(tuple_1, tuple_2))
# [1,2,3,4,5,6]



#6
dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
    dict_2[dict_values[i]] = dict_keys[i] # {1:2, 2:4, 3:6

print(dict_2[2])
#4



#7
animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i] # {4:cat, 0:snake, 2:monkey, 4:ant, 8:spider}
	animal_legs_dict['ant'] = 6

print(animal_legs_dict)
# {4:cat, 0:snake, 2:monkey, 4:ant, 8:spider, ant:6}
# 동일한 키가 존재하면 안됨
# {4:ant, 0:snake, 2:monkey, 8:spider, ant:6}



#8
Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)
#10



#9
a = list(range(10)) #(0,1,2,3,4,5,6,7,8,9)
a.append(a[3])
a.pop(a[3])
a.insert(3, a[-1])
a.pop()
print(a)



#10
data_1 = {'one' : (1,2,3,4,5,6),
          'two' : [1,2,3,4,5,6],
          'three' : {'four' : 4, 'five' : 5}
          }
for k in ['one','two','three']:
	try:
		print(data_1[k][:1]) # {one:1, two:1,
	except TypeError:
		print("error")

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		print(data_1[k][-1])
	except TypeError :
		print("error")