

# 함수 연습문제 ==========

print()
# 1 =======================
def test(t):
	t = 20
	print ("In Function:", t)

x = 10
print ("Before:", x)
test(x)
print ("After:", x)

# Before: 10
# In Function: 20
# After: 10


print()
# 2 =======================
def sotring_function(list_value):
	return list_value.sort()

print(sotring_function([5,4,3,2,1]))
# None > return값을 받지 않음


print()
# 3 =======================
def is_yes(your_answer):
	if your_answer.upper() == "YES" or you_answer.upper() == "Y":
		result = your_answer.lower()
		# print(result)

print(is_yes("Yes"))
# None > result값을 출력하지 않음



print()
# 4 =======================
def add_and_mul(a, b, c):
	return b + a * c + b

print(add_and_mul(3, 4, 5) == 63)
# False

'''
print()
# 5 =======================
def args_test_3(one, two, *args, three):
	print(one + two + sum(args))
	print(args)

args_test_3(3, 4, 5, 6, 7)

# 19
# (5, 7)
'''


print()
# 6 =======================
def rain(colors):
	colors.append("purple")
	colors = ["green", "blue"]
	return colors

rainbow = ["red", "orange"]
print(rain(rainbow))

# ["green", "blue"]



print()
# 7 =======================
def function(value):
    print(value ** 3)
print(function(2))
# 8
# None



print()
# 8 =======================
def get_apple(fruit):
	fruit = list(fruit)
	fruit.append("e")
	fruit = ["apple"]
	return fruit

fruit = "appl"
get_apple(fruit)
print(fruit)
# ["apple"]


print()
# 9 =======================
def return_sentence(sentence, n):
	sentence += str(n)
	n -= 1
	if n < 0:
		return sentence
	else:
		return(return_sentence(sentence, n))

sentence = "I Love You"
print(return_sentence(sentence, 5))
#I Love You543210



print()
# 10 =======================
def test(x, y):
	tmp = x
	x = y
	y = tmp
	return y.append(x)

x = ["y"]
y = ["x"]
test(x, y) # return값을 받지 않았기때문에
print(y) #['x']



print()
# 11 =======================
def factorial_calculator(n):
	if n in (0, 1):
		return 1
	else:
		return n * n-1

print(factorial_calculator(5))
