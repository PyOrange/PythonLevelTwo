# 객체 지향 프로그램(Object-Oriented Programming) = 코드의 재사용 및 중복 방지, 유지보수 편리
# 규모가 큰 프로젝트(프로그램) = 함수 중심 = 데이터 방대 = 문제 복잡
# 클래스 중심 = 데이터 중심 = 객체로 관리

# 일반적 코딩

# 차량 1
car1 = "a"
detail1 = [
    {'color' : 'red'},
    {'price' : 100}
]

# 차량 2
car2 = "b"
detail2 = [
    {'color' : 'yellow'},
    {'price' : 200}
]

# 리스트 구조
# 인덱스 번호를 통한 접근 = 관리가 불편
carList = ["a", "b", "c", ...]
detailList = [
    {"color" : "red", "price" : 100},
    {"color" : "yellow", "price" : 200}
]

del carList[2]
# print(carList)
# 결과 = ['a', 'b', Ellipsis]

# print() # 줄바꿈

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외처리 등

carDict = [
    {"car" : "a", "detail" : {"color" : "red", "price" : 100}},
    {"car" : "b", "detail" : {"color" : "yellow", "price" : 200}}
]
# print(carDict)
# 결과 = [{'car': 'a', 'detail': {'color': 'red', 'price': 100}}, {'car': 'b', 'detail': {'color': 'yellow', 'price': 200}}]

del carDict[1]
# print(carDict)
# 결과 = [{'car': 'a', 'detail': {'color': 'red', 'price': 100}}]

# print() # 줄바꿈


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드반복 최소화, 메서드 활용
class Car():
    """
    자동차 클래스
    만든 이 = 오렌지
    """
    # 클래스 변수 = 모든 인스턴스가 공유
    count = 0
    tax = 1.5
    
    # 인스턴스 메서드
    def __init__(self, car, detail):
        self.car = car
        self.detail = detail
    
    # 인스턴스 메서드
    # 객체값을 문자열로 반환(변경)
    def __str__(self):
        return "str : {} - {}".format(self.car, self.detail)
    
    # 인스턴스 메서드
    # self = 객체의 고유한 속성값 사용 
    # 객체값의 정보 출력
    def info(self):
        print("id : {}".format(id(self)))
    
    # 인스턴스 메서드
    def getPrice(self):
        return "before : car : {}, price : {}".format(self.car, self.detail.get("price"))

    # 인스턴스 메서드
    def getPrice2(self):
        return "after : car : {}, price : {}".format(self.car, self.detail.get("price") * Car.tax)
    
    # 클래스 메서드
    @classmethod
    def raiseTax(cls, per):
        Car.tax
    

# 인스턴스 생성
car1 = Car("a", {"color" : "red", "price" : 100})
car2 = Car("b", {"color" : "yellow", "price" : 200})
# print(car1)
# 결과 : str : a - {'color': 'red', 'price': 100} 

# print(car1.__str__())
# 결과 = str : a - {'color': 'red', 'price': 100}

# dir = 객체(없으면 전체)가 가지고 있는 속성(변수)과 메서드(함수) 목록을 반환
# print(dir(car1))

# print(car1.__dict__)
# {'car': 'a', 'detail': {'color': 'red', 'price': 100}}

# 클래스 기반의 리스트 선언
carList2 = []
carList2.append(car1)

# carList2의 모든 요소를 x에 저장
# for x in carList2:
    # x의 요소를 문자열로 변환해서 출력
    # print(str(x))
# 결과 = str : a - {'color': 'red', 'price': 100}

# id 확인
# print(id(car1))
# 결과 = 2001746290944

# print(car1.car == car1.detail)
# False

# __doc__ = 클래스에 적힌 주석 확인
# print(Car.__doc__)
# 자동차 클래스
# 만든 이 = 오렌지

# car1.info()
# id : 1541902461184

# 비교
# print(id(car1.__class__), id(car2.__class__))
# 1727317680416 1727317680416

# 에러
# Car.info()
# TypeError: Car.info() missing 1 required positional argument: 'self'

# Car.info(car1)
# id : 2743649724672

# 클래스 인스턴스 출력
# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 상위(클래스 변수, 부모클래스 변수))
# print(Car.count)
# 0

# 가격정보 출력(직접 접근)
#(비추) print(car1.detail.get("price")) 
#(비추) print(car1.detail["price"]) 

# 가격정보 출력(메서드 활용)
print(car1.getPrice())
print(car1.getPrice2())
# before : car : a, price : 100
# after : car : a, price : 150.0



