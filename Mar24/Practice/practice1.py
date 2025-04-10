# 클래스를 활용한 관리
# class Car():
#     # 속성을 관리할 생성자 메서드
#     def __init__(self, company, details):
#         self._company = company
#         self._details = details

#     # Print() 또는 객체를 직접 출력할 때 사용자 친화적인 형식으로 객체를 표현합니다. (GPT)
#     def __str__(self):
#         return 'str : {} - {}'.format(self._company, self._details)
    
#     # 객체를 직접 출력할 때 개발자가 이해하기 쉬운 방식으로 표현합니다. (GPT)
#     def __repr__(self):
#         return 'repr : {} - {}'.format(self._company, self._details)
    
#     # 객체의 정보를 출력
#     def detail_info(self):
#         print('Current Id : {}'.format(id(self)))
#         print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
#     # 이전 차값 출력
#     def get_price(self):
#         return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

#     # 오른 후 차값 출력
#     def get_price_culc(self):
#         return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
# # 클래스 기반의 인스턴스 선언
# car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
# car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
# car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# # 인스턴스 고유의 id 출력
# print(id(car1))
# print(id(car2))
# print(id(car3))

# # 두 인스턴스간 비굣값 출력(boolean)
# print(car1._company == car2._company)
# print(car1 is car2)

# # dir & __dict__ 확인
# print(dir(car1))
# print(dir(car2))

# print()
# print()

# # 인스턴스가 사용가능한 메서드 종류 출력
# print(car1.__dict__)
# print(car2.__dict__)

# # 클래스나 메서드 내부에 있는 주석 출력
# print(Car.__doc__)
# print()

# # 실행
# car1.detail_info()
# car2.detail_info()

# # 에러
# # Car.detail_info()
# Car.detail_info(car1)
# Car.detail_info(car2)

# # 두 인스턴스간 비굣값 출력(boolean)
# print(car1.__class__, car2.__class__)
# print(id(car1.__class__) == id(car3.__class__))

# print()

# # 인스턴스의 속성 출력
# print(car1._company, car2._company)
# print(car2._company, car3._company)

# print()
# print()

# # 클래스 내 속성 출력
# print(car1.car_count)
# print(car2.car_count)
# print(Car.car_count)

# print()
# print()


# # 공유 확인
# print(Car.__dict__)
# print(car1.__dict__)
# print(car2.__dict__)
# print(car3.__dict__)

# del car2

# print(car1.car_count)
# print(Car.car_count)


# # 기본 정보
# print(car1)
# print(car2)
# print()

# # 전체 정보
# car1.detail_info()
# car2.detail_info()
# print()

# # 가격 정보(인상 전)
# print(car1.get_price())
# print(car2.get_price())
# print()

# # 가격 인상(클래스 메서드 미사용)
# Car.price_per_raise = 1.2

# # 가격 정보(인상 후)
# print(car1.get_price_culc())
# print(car2.get_price_culc())
# print()

# # 가격 인상(클래스 메서드 사용)
# Car.raise_price(1.6)
# print()

# # 가격 정보(인상 후 : 클래스 메서드)
# print(car1.get_price_culc())
# print(car2.get_price_culc())
# print()

# # Bmw 여부(스태틱 메서드 미사용)
# def is_bmw(inst):
#     if inst._company == 'Bmw':
#         return 'OK! This car is {}.'.format(inst._company)
#     return 'Sorry. This car is not Bmw.'

# # 별도의 메소드 작성 후 호출
# print(is_bmw(car1))
# print(is_bmw(car2))
# print()

# # Bmw 여부(스태틱 메서드 사용)
# print('Static : ', Car.is_bmw(car1))
# print('Static : ', Car.is_bmw(car2))
# print()

# print('Static : ', car1.is_bmw(car1))
# print('Static : ', car2.is_bmw(car2))

"""
    [Q] 클래스 메서드는 어떤 종류가 있을까? 언제 사용할까? :: 각 종류에 대한 설명과 예제 1가지
        - 기본적인 메서드 : 가장 기본인 메서드이며, 보통 self로 인스턴스 변수를 조작할 때 사용
        - Static 메서드 : @staticmethod가 필요하며, 클래스와 크게 관계없는 유틸리티 기능을 만들 때 사용
        - 기타 종류 : 매직 메서드(클래스 기본제공 기능), 프라이빗 메서드(_ 또는 __, 외부에서 직접 호출 불가능) 등이 있음
        예시 : 
            class MyClass:
                count = 0  # 클래스 변수

            def __init__(self, name): # 매직 메서드, 프라이빗 메서드, 인스턴스 메서드
                self.name = name   
                MyClass.count += 1

            def greet(self):  # ✅ 인스턴스 메서드
                return f"안녕하세요, {self.name}입니다."

            @staticmethod
            def add(a, b):  # ✅ 스태틱 메서드
                return a + b

            def __str__(self):  # ✅ 매직 메서드, 프라이빗 메서드, 인스턴스 메서드
                return f"MyClass 인스턴스: {self.name}"

"""

# 예제
class person:
    
    count = 0
    # 매직 메서드, 프라이빗 메서드, 인스턴스 메서드
    def __init__(self, name, age):
        self.name = name
        self.age = age
        person.count += 1
        
    # 매직 메서드, 프라이빗 메서드, 인스턴스 메서드
    def __str__(self):
        return f"name : {self.name}, age : {self.age}"
    
    # 스태틱 메서드, 인스턴스 메서드
    @staticmethod
    def mul(self):
        return self.age * person.count

person1 = person("k", 1)
print(person.count)

