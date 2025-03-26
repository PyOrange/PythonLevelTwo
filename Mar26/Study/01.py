# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화 
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능

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
print(list(map(var_func, range(1,6))))


print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])

print()
print()

# reduce() : 반복 가능한 값을 하나의 변수로 만듦
from functools import reduce
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

from inspect import signature

sg = signature(var_func)

print(sg)
print(sg.parameters)

print()
print()

# partial : 기존 숫자를 고정하거나 재사용 
from operator import mul
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


# 예
def func_v1(a):
    print(a)
    print(b)

# 예외 : 직접 숫자 넣는건 안됨
# func_v1(10)

# 예2
b = 20

def func_v2(a):
    print(a)
    print(b)

func_v2(10)


# Ex3

c = 30

def func_v3(a):
    global c
    print(a)
    print(c)
    c = 40
    
print('>>',c)
func_v3(10)
print('>>>',c)

from dis import dis

print()
print(dis(func_v3))

print()
print()


a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,101)))

print()
print()

# 클래스를 활용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()

# 누적
print(averager_cls(15))
print(averager_cls(35))
print(averager_cls(40))

print()
print()

# 클로저(Closure) 사용
def closure_ex1():
    # Free variable
    series = []
    # 클로저 영역
    def averager(v):
        # series = [] # 주석 해제 후 확인
        series.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    
    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()

# function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()


# 잘못된 클로저 사용
def closure_ex2():
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1 # cnt = cnt + 1
        total += v
        return total / cnt
    
    return averager

avg_closure2 = closure_ex2()

# print(avg_closure2(15)) # 예외


# Nonlocal : 메서드 밖에 있는 변수 가져옴
def closure_ex3():
    cnt = 0
    total = 0
    
    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()

# 데코레이터 실습
import time

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간 
        st = time.perf_counter() 
        result = func(*args)
        # 함수 종료 시간 계산
        et = time.perf_counter() - st 
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수 
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result)) 
        return result 
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미사용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-' * 40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-' * 40, 'Called None Decorator -> sum_func')
print()
none_deco2(100, 150, 250, 300, 350)

print()
print()


# 데코레이터 사용
print('*' * 40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('*' * 40, 'Called Decorator -> sum_func')
print()
sum_func(100, 150, 250, 300, 350)
print()