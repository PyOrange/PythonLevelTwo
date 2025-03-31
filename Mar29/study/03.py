
# 스레드 : os가 관리하는 일꾼
# 코루틴 : 단일 스레드 느낌, yield를 통해 중단했다가 다시 실행 가능하다는 장점이 있음
# 장점2 : 메모리를 절약하면서 큰 데이터도 효율적으로 처리 가능
# yield : 제네레이터를 만들 때, 값의 실행 상태를 저장해서 반환 

# 코루틴 예1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언
cr1 = coroutine1()

# 타입 출력
print(cr1, type(cr1))

# next(cr1)

# next(cr1)

# cr1.send(100)

# 제네레이터 선언
cr2 = coroutine1()

# cr2.send(100)

# 코루틴 예2
def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

print(cr3.send(15))

# print(c3.send(20))

print()
print()

def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()

# A부터 한 글자씩 출력 
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()

# 제네레이터1의 yield 리스트 출력
print(list(t2))

print()
print()

# yield from : 복수의 제네레이터(또는 이터레이터)를 자동으로 처리
# for 반복문 없이도 위와 같은 기능을 수행
def generator2():
    yield from 'AB'
    yield from range(1,4)


t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))

print()
print()