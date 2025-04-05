

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
    
    # 인스턴스의 특정 속성만 사용해 표현
    def proper(self):
        return "해당 상품의 크기는 {}L 입니다.".format(self.size)
    

# 인스턴스 생성
water = Water("a", "b", 1)

# 클래스 메서드 실행
print(water.proper())

"""
    [Q] 클래스 메서드는 어떤 종류가 있을까? 언제 사용할까? :: 각 종류에 대한 설명과 예제 2가지씩!
        - 기본적인 메서드
        - Static한 메서드
        - 기타 종류
"""