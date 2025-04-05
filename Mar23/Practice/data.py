
"""
    [Q] 데이터 관리 방식에 따라 어떤 차이점(장단점)이 있을까? :: 각각 어떤 상황에 사용하면 좋은지 설명과 예시 2가지!
    - 리스트를 통한 관리 : 
        장점 : 간단한 사용 가능, 데이터의 순서가 중요하거나 반복 작업을 할 때 유용
        단점 : 인덱스 번호로만 데이터를 관리, 데이터가 많아질수록 가독성 감소
        사용 : 데이터를 순서대로 반복 작업할 때 주로 사용
        예시 : 
            # 인스턴스 생성
            students = [["홍길동", 90], ["김철수", 85]]
            
            # 반복문을 활용한 작업
            for student in students:
                print(f"{student[0]}의 점수는 {student[1]}점입니다.")

        
    - 딕셔너리를 통한 관리 : 
        장점 : 데이터를 검색하거나 알아보는데 유용
        단점 : 데이터가 많아질수록 복잡
        사용 : 데이터를 조회 또는 수정하는데 사용
        예시 : 
            # 인스턴스 생성
            student = {"name": "홍길동", "score": 90}
            
            # 데이터 검색을 활용한 작업
            print(f"{student['name']}의 점수는 {student['score']}점입니다.")

        
    - Class 객체를 통한 관리 : 
        장점 : 객체 지향적 관리(Java처럼), 유지보수 및 안정성 확보 유리
        단점 : 단순한 코드엔 과한 작업, 다양한 기능이 포함되어 복잡해질 가능성
        사용 : 복잡하고 많은 데이터 관리, 그에 맞는 기능 포함할 때 사용
        예시 : 
            # 클래스 선언
            class Student:
            
            # 생성자 메서드
                def __init__(self, name, score):
                    self.name = name
                    self.score = score
                    
                # 점수 출력하는 메서드
                def print_score(self):
                    print(f"{self.name}의 점수는 {self.score}점입니다.")

            # 클래스 밖에서 인스턴스 생성
            s = Student("홍길동", 90)
            
            # 클래스 내부의 메서드 호출
            s.print_score()

"""

# 예제
# 리스트를 활용한 관리
person1 = ["kim", 20, "men"]
person2 = ["park", 10, "boy"]

print(person1[1])
print(person1 == person2)


# 딕셔너리를 활용한 관리
person3 = {"name" : "kim", "age" : 20}
person4 = {"name" : "choi", "age" : 50}

print(person3)
print(person3.get("name"))


# 클래스를 활용한 관리
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
person5 = Person("kim", 40)
print(person5.getName())



"""
    [Q] __str__ 과 __repr__ 을 둘 다 정의하면, 객체 출력 시 어떤 게 동작할까? :: 테스트를 통해 동작 우선권 이해하기 :
        print()를 통해 출력할 때는 __str__(없을 경우 __repr__), 객체를 직접 출력할 때는 __repr__ 메서드가 동작함
        예시 : 
            class Person:
                def __str__(self):
                    return "사용자 친화적 문자열"

                def __repr__(self):
                    return "개발자용 문자열"

            p = Person()

            print(p)      # 사용자 친화적 문자열
            p             # 개발자용 문자열 (인터프리터에서는 repr 호출)

    [Q] 둘 다 만들어서 하나만 동작한다면, 둘 다 만들 필요가 있을까? : 
        있겠니
    
    [Q] 두 메서드는 언제 사용할까? :: 현업에서는 둘을 어떻게 사용하는지의 예시 1가지 :
        두 메서드 모두 출력되는 메세지 내용을 바꾼다는 공통점이 있기에, 
        사용자에게 보기 편하게 보여줄 때는 __str__, 개발자에게 적합하게 출력할 때는 __repr__을 주로 사용
        예시 : 
            
            class Product:
                def __init__(self, name, price):
                    self.name = name
                    self.price = price

                def __str__(self):
                    return f"{self.name} - {self.price}원"
                    
                def __repr__(self):
                    return f"Product(name={self.name!r}, price={self.price})"

            p = Product("무선 마우스", 19900)
            print(p)  # 무선 마우스 - 19900원
            
            products = [Product("키보드", 29900), Product("헤드셋", 49900)]
            print(products)
            # [Product(name='키보드', price=29900), Product(name='헤드셋', price=49900)]
"""

# 예제
class Log:
    def __init__(self, type, status):
        self.type = type
        self.status = status
        
    def __str__(self):
        return f"응애 나 {self.status} {self.type}!"
    
    def __repr__(self):
        return f"method launched : Log.__repr__, type : {self.type}, status : {self.status}"
    
cat = Log("cat", "hungry")

print(cat)
print(repr(cat))
