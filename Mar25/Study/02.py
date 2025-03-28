
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