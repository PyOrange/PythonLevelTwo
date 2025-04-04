# 일급 함수
# 필요한 조건:
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 결과 반환 가능


# 함수 객체
def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

# 팩토리얼 : 확통 그 팩토리얼 ㅇㅇ
print(factorial(6))

# 설명 출력
print(factorial.__doc__)

# 타입 출력
print(type(factorial), type(A))

# 중복되는거 제외 사용가능한 매직메서드 출력
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))

# 이름이랑 코드 출력
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수1 = 아까 설정한 팩토리얼
var_func = factorial

# 활용
print(var_func)
print(var_func(10))
print(map(var_func, range(1,11)))

# map, filter 활용
# map : 반복 가능한 객체의 각 요소에 함수를 적용하여 새로운 값을 생성?
# filter : 특정 조건으로 필터링 반복작업
print(list(map(var_func, range(1,6))))
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])

print()
print()

# reduce() : 반복 가능한 값을 하나의 변수로 만듦
from functools import reduce
# add = +
from operator import add

# 1 + 2 + 3 + ... + 11
print(reduce(add, range(1,11))) 
print(sum(range(1,11)))


# 람다 : 함수를 선언할때 사용, 기존 메서드 선언보다 간단함에 특화
print(reduce(lambda x, t: x + t, range(1,11)))

print()
print()

# Callable : 호출 연산자 : 메소드 형태로 호출 가능한지 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))

# signature : 클래스 또는 메서드 내의 변수를 추출하는데 유용
from inspect import signature

sg = signature(var_func)

print(sg)
print(sg.parameters)

print()
print()

# mul = *
from operator import mul
# partial : 기존 숫자를 고정, 반복적으로 같은 연산을 수행하기 편함
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5)

# 추가로 고정
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))


# 파이선 변수 범위 예제1
def func_v1(a):
    print(a)
    print(b)

# 에러 : b 없음
# func_v1(10)

# 예시2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# 예시3

c = 30

def func_v3(a):
    # global : 밖에 있는 변수 참조
    global c
    print(a)
    print(c)
    c = 40
    
print('>>',c)
func_v3(10)
print('>>>',c)

