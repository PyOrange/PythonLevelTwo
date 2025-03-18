class Human:
    '''
    사람 클래스 / 매직 메서드 실험용 클래스
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return "저는 {}살 {}입니다.".format(self.age, self.name)
    
    def __add__(self, i):
        return (self.age + i.age) * 2
    
    def __sub__(self, i):
        return (self.age - i.age) * 1.9 / 40 + 64
    
    def __mul__(self, i):
        return self.age * i.age
    
    def __truediv__(self, i):
        return self.age / i.age
    
    def __le__(self, i):
        if self.age == i.age:
            return True
        else:
            return False

a = Human("a", 10)
b = Human("b", 91)
c = Human("c", 47)
d = Human("d", 401)

print(a + b) # 202
print(c - d) # 47.185
print(a * c) # 470
print(d / a) # 40.1
