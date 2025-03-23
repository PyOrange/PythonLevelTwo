

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
        return "이름 : {}, 종류 : {}, 크기 : {}".format(self.name, self.type, self.size)
    
    # 객체를 직접 출력할 때 개발자가 이해하기 쉬운 방식으로 표현합니다. (GPT)
    def __repr__(self):
        return "이름 : {}, 종류 : {}, 크기 : {}".format(self.name, self.type, self.size)

# 클래스 기반의 인스턴스 선언
water3 = Water("SamDaSu", "water", 0.5)

# Water 인스턴스 출력
print(water3)




