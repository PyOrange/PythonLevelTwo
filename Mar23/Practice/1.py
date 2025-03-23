

# 여러가지 방법의 데이터 관리

# 일반적인 관리
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color' : 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]


# 리스트를 활용한 관리
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower': 400, 'price': 8000},
    {'color' : 'Black', 'horsepower': 270, 'price': 5000},
    {'color' : 'Silver', 'horsepower': 300, 'price': 6000}
]
# 같은 데이터도 관리 방식에 따라 장단점이 존재

# 해당 번호의 데이터 삭제
del car_company_list[1]
del car_detail_list[1]

# 해당 리스트 전체 출력
print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리를 활용한 관리
cars_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color' : 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color' : 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color' : 'Silver', 'horsepower': 300, 'price': 6000}}
]

# 딕셔너리 내 해당 번호의 데이터 삭제
del cars_dicts[1]

# 딕셔너리 전체 출력
print(cars_dicts)

print()
print()


# 클래스를 활용한 관리
class Car():
    # 속성을 관리할 생성자 메서드
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # Print() 또는 객체를 직접 출력할 때 사용자 친화적인 형식으로 객체를 표현합니다. (GPT)
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)
    
    # 객체를 직접 출력할 때 개발자가 이해하기 쉬운 방식으로 표현합니다. (GPT)
    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)
    
# 클래스 기반의 인스턴스 선언
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 파이썬 객체의 속성을 저장하는 딕셔너리 출력 (GPT)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 리스트 선언
car_list = []

# 리스트 내에 데이터 추가
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 줄넘김
print()

print(car_list)

print()
print()

# 리스트 내 반복작업
for x in car_list:
    print(repr(x))
    print(x)