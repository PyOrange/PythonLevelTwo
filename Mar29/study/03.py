
# 스레드 : os가 관리하는 일꾼
# 코루틴 : 단일 스레드 느낌, yield를 통해 중단했다가 다시 실행 가능
# yield : 제네레이터를 만들 때, 값의 실행 상태를 저장해서 반환 
# 장점 : 메모리를 절약하면서 큰 데이터도 효율적으로 처리 가능
# yield from

# 코루틴 Ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# next(cr1)

# next(cr1)

# cr1.send(100)


cr2 = coroutine1()

# cr2.send(100)

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

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()

print(list(t2))

print()
print()

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