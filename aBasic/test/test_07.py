

# 1- 리스트를 인자로 받아 짝수만 갖는 리스트 반환하는 함수를 만들어서 호출하여 그 결과를 출력하시오
evenlist = []
def even_filter(list):
    for i in range(1,7):
        if list[i] % 2 == 0 :
            evenlist.append(list[i])
        else:
            continue

print(even_filter([1, 2, 4, 5, 8, 9, 10]))
print(evenlist)