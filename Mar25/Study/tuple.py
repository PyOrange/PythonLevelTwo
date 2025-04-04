# 리스트 생성자?기계? 생성 
import array

# 튜플 : 값을 변경할 수 없는 순서가 있는 자료
# 리스트보다 빠르고 데이터 중복을 허용한다는 장점
# 튜플로 한 번에 한 개의 항목을 생성(메모리 유지 안됨)
chars = '+_)(*&^%$#@!~)'
# 튜플로 객체 생성
tuple_g = (ord(s) for s in chars)
# array로 객체 생성
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

# 얕은복사(copy) : 기존 객체를 공유하는 객체 생성(수정 시 원본에 영향 ㅇㅇ)
# 깊은복사(deepcopy) : 기존 객체와 처음 값만 같은 객체 복사(수정 시 원본에 영향 ㄴㄴ) 
# '~'인자를 가진 서로 다른 객체 5개 생성(깊은복사)
marks1 = [['~'] * 5 for n in range(5)]

# '~'인자를 가진 깉은 객체 5개 복사(얕은복사)
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


# divmod : a를 b로 나눈 몫과 나머지 출력
print(divmod(100, 9))
# 튜플로 실행할 경우 * 넣어줘야함
print(divmod(*(100, 9)))
# 언패킹(괄호 벗겨져서 나옴)
print(*(divmod(100, 9)))

print()

# 1, 2는 각각 x, y로 할당, 나머지는 rest에 리스트 형태로 할당
x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()


# sorted : 정렬된 새로운 객체 반환
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

# sort : 정렬된 객체 직접 변경

# 반환 값 확인(None)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)