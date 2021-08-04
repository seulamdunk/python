
a = 11
b = 9
print('a' + 'b')


print()
fact = "Python is funny"
print(fact.find('n'))
print(fact.rfind('n')) # 오른쪽 왼쪽으로부터 n (왼쪽에서부터 위치)
print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))
# 3 + 5 + 13


print()
text = 'Gachon CS50 - programming with python'
text2 = " Human cs50 knowledge belongs to the world "
text.lower()
print(text2.split()[0])
print(text[:5])
print(text[:5] + text[-1] + text[6] + text2.split()[0])
# Gacho + n + + Human


print()
class_name = 'introduction programming with python'
for i in class_name:
    if i == 'python':
        i = i.upper()
print(class_name)
#introduction programming with python


a = '10'
b = '5-2'.split('-')[1] #2
print(a * 3 + b)
# 1010102


print()
a = "abcd e f g"
b = a.split() # 'abcd' 'e' 'f' 'g'
c = (a[:3][0]) #abc > a
d = (b[:3][0][0]) # a
print(b)
print(c)
print(d)
print(c + d) #abcaabcaa



result = "CODE2018"
print("{0},{1}".format(result[-1], result[-2]))