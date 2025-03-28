

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
# filter는 함수와 자료구조형 데이터를 받음
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

# 튜플 : 값을 변경할 수 없는 순서가 있는 자료
# 리스트보다 빠르고 데이터 중복을 허용한다는 장점
# 튜플로 한 번에 한 개의 항목을 생성(메모리 유지 안됨)
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

# for문을 활용한 예제
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print(s)

print()
print()

# 리스트 주의 (깊은복사 앝은복사?)
# '~'인자를 가진 서로 다른 객체 5개 생성
marks1 = [['~'] * 5 for n in range(5)]

# '~'인자를 가진 깉은 객체 5개 복사
marks2 = [['~'] * 5] * 5

print(marks1)
print(marks2)

print()

# 첫 번째 객체에서만 수정됨
marks1[0][1] = 'X'

# 모든 객체에서 동일하게 수정됨
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 확인 겸 출력
print([id(i) for i in marks1])
print([id(i) for i in marks2])

