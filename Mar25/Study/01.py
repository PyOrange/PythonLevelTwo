

# 기존의 리스트
chars = '+_)(*&^%$#@!~)'
code_list1 = []

for s in chars:
    # 유니코드를 담아놓은 리스트
    code_list1.append(ord(s))

# 지능형 리스트 : 기존의 리스트보다 더 간단하게 생성 및 활용 가능
code_list2 = [ord(s) for s in chars]

# 아래가 속도가 조금 더 빠름
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()


# 리스트 생성자?기계? 생성 
import array

# 한 번에 한 개의 항목을 생성(메모리 유지 안됨)
tuple_g = (ord(s) for s in chars)
# 배열로
array_g = array.array('I',  (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())

print()
print()

# 리스트 메이커? 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)


print()
print()

# 리스트 주의
marks1 = [['~'] * 5 for n in range(5)]
marks2 = [['~'] * 5] * 5

print(marks1)
print(marks2)

print()

# 수정 가능
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 확인 겸 출력
print([id(i) for i in marks1])
print([id(i) for i in marks2])

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()


# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# 람다 : 함수를 선언할때 사용, 기존 메서드 선언보다 간단함에 특화
print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True))
print('sorted -', sorted(f_list, key=len))
print('sorted -', sorted(f_list, key=lambda x: x[-1]))
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()

print('sorted -', f_list)

print()

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
