

# 여러가지 방법의 데이터 관리

# 일반적인 관리
water1 = "SamDaSu"
water1_details = [
    {"type" : "water"},
    {"size" : 0.5}
]

# 리스트를 활용한 관리
waterList = ["SamDaSu", "CocaCola", "etc"]
detailList = [
    {"type" : "water", "size" : 0.5},
    {"type" : "soda", "size" : 1.5}
]
# 같은 데이터도 관리 방식에 따라 장단점이 존재

"""
    [Q] 데이터 관리 방식에 따라 어떤 차이점(장단점)이 있을까? :: 각각 어떤 상황에 사용하면 좋은지 설명과 예시 2가지!
    - 리스트를 통한 관리
    - 딕셔너리를 통한 관리
    - Class 객체를 통한 관리
"""

# 해당 번호의 데이터 삭제 
del waterList[1]

# 해당 리스트 전체 출력
print(detailList)


# 딕셔너리를 활용한 관리
waterDict = [
    {"water" : "SamDaSu", "details" : {"type" : "water", "size" : 0.5}},
    {"water" : "CocaCola", "details" : {"type" : "soda", "size" : 1.5}}
]

# 딕셔너리 전체 출력
print(waterDict)

# 딕셔너리 내 해당 번호의 데이터 삭제
del waterDict[1]
print(waterDict)


# 클래스를 활용한 관리
class Water:
    # 속성을 관리할 생성자 메서드
    def __init__(self, name, type, size):
        self.type = type
        self.name = name
        self.size = size
        
    # Print() 또는 객체를 직접 출력할 때 사용자 친화적인 형식으로 객체를 표현합니다. (GPT)
    def __str__(self):
        return "str) 이름 : {}, 종류 : {}, 크기 : {}".format(self.name, self.type, self.size)
    
    # 객체를 직접 출력할 때 개발자가 이해하기 쉬운 방식으로 표현합니다. (GPT)
    def __repr__(self):
        return "repr) 이름 : {}, 종류 : {}, 크기 : {}".format(self.name, self.type, self.size)

# 클래스 기반의 인스턴스 선언
water3 = Water("SamDaSu", "water", 0.5)

# Water 인스턴스 출력
print(water3)

"""
    [Q] __str__ 과 __repr__ 을 둘 다 정의하면, 객체 출력 시 어떤 게 동작할까? :: 테스트를 통해 동작 우선권 이해하기
    
    [Q] 둘 다 만들어서 하나만 동작한다면, 둘 다 만들 필요가 있을까?
    
    [Q] 두 메서드는 언제 사용할까? :: 현업에서는 둘을 어떻게 사용하는지의 예시 2가지!
"""


