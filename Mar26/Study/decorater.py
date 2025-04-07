# 데코레이터 : 함수를 수정하지 않고 기능을 추가
# 장점 : 재사용성 향상, 권한 검사, 시간 측정에 용이
# 단점 : 남발시 가독성 감소, 한 번만 사용되는 함수에 부적절 

# 데코레이터 실습
import time

def perf_clock(func):
    # 클로저
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
    
"""
    [Q] 데코레이터를 사용해서 아래의 기능을 구현해 주세요.
    - 메서드 실행 중, 예외 발생 시 "예외 발생!" 이라고 출력해주는 기능
    - 메서드 실행 성공/실패 여부와 소요 시간을 출력해주는 기능
"""

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