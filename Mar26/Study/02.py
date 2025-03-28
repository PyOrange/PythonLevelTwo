
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

# 클로저 : 메서드 내의 변수 상태(값) 기억, 변경되지 않음
# 사용 이유 : 동시 접속 시 터지는거 대비 제어를 쉽게 함
#             따라서 여러 일을 동시에 실행하는데 강점
# dis : 바이트코드 분석, 최적화 및 디버깅에 유용
from dis import dis

print()
print(dis(func_v3))

print()
print()


a = 100

print(a + 100)
print(a + 1000)

# sum : 결과 누적
print(sum(range(1,51)))
print(sum(range(51,101)))

print()
print()

# 클래스를 활용
# 값을 누적시켜 평균을 구하는 클래스
class Averager():
    def __init__(self):
        self._series = []

# call : 클래스를 함수처럼 쓸 수 있게 해주는 매직 메서드
    def __call__(self, v):
        self._series.append(v)
        print('inner >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()

# call 메서드를 통해 클래스를 함수처럼 활용
print(averager_cls(15))
print(averager_cls(35))
print(averager_cls(40))

print()
print()

# 클로저 사용
# 값을 누적시켜 평균을 구하는 클래스
def closure_ex1():
    series = []
    # 클로저 영역 : 메서드 바깥에 있는 자유 변수에도 접근 및 저장 가능
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

# 함수 내부 조사

# 구현할 수 있는 함수 목록 출력
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
        # 이 메서드의 변수와 바깥에 있는 변수가 같다고 할 수 없음
        # = len
        cnt += 1 # cnt = cnt + 1
        # = sum
        total += v
        return total / cnt
    
    return averager

avg_closure2 = closure_ex2()

# 에러 : 위의 자유변수를 참조하지 못함
# print(avg_closure2(15))

# 잘못된 예시를 실행되게 변경
def closure_ex3():
    cnt = 0
    total = 0
    
    def averager(v):
        # Nonlocal : 메서드 밖에 있는 변수 가져옴
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure3 = closure_ex3()

# 예제2 와는 다르게 실행 가능
print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()