# 스페셜(매직) 메서드
# 파이선의 핵심 = 시퀀스(Sequence), 반복(Iterator), 클래스(Class), 함수(Function)
# 클래스 안에 정의가능한 특별한(Built-In) __메서드__


# 기본형
print(int) # <class 'int'>
print(float) # <class 'float'>

# 모든 속성 및 메서드 출력
print(dir(int)) # ['__abs__', '__add__', '__and__', ...
print(dir(float)) # ['__abs__', '__add__', '__bool__', ...

n = 10

print(n + 100) # 110
print(n.__add__(100)) #110
# 둘이 실제로 수행하는 기능은 같다

print(n.__doc__) # 속성의 타입(클래스) 정의 확인
print(n.__bool__(), bool(n)) # True True
print(n * 100, n.__mul__(100)) # 1000 1000

print() # 줄바꿈
print() # 줄바꿈


# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "Info : {} - {}".format(self.name, self.price)
    
    # 덧셈  
    def __add__(self, i):
        print("print") # print
        return self.price + i.price * 0.9
    
    # 뺄셈
    def __sub__(self, i):
        return self.price - i.price
    
    # 비교
    def __le__(self, i):
        if self.price < i.price:
            return True
        else:
            return False
    
# 인스턴스 생성
s1 = Fruit("apple", 5000)
s2 = Fruit("orange", 6000)

print(s1 + s2) # 10400.0

# 매직 메서드
print(s1 <= s2) # True
print(s1 >= s2) # False


# 클래스 예제2
# 벡터(x, y) 연산
class Vector(object):
    def __init__(self, *args):
        """
        벡터를 만드는 클래스
        """
        if len(args) == 0:
            self.x, self.y = 0, 0
        else : 
            self.x, self.y = args
            
    # 벡터 정보 반환
    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)
    
    # 벡터 덧셈
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # 벡터 곱셈
    def __mul__(self, y):
        return Vector(self.x * y, self.y * y)
    
    # 벡터 최댓값 반환
    def __bool__(self): 
        return bool(max(self.x, self.y))
    
    
v1 = Vector(1, 1)
v2 = Vector(2, 3)

# 매직 메서드 출력
print(Vector.__init__.__doc__) # 벡터를 만드는 클래스

print(v1, v2) # Vector(1, 1) Vector(2, 3)
print(v1 + v2) # Vector(3, 4)
print(v1 * 3) # Vector(3, 3)
print(bool(v1), bool(v2)) # True True


