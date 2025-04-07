

# 지능형 리스트 실습

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetList = []

for a in alphabetList:
    alphabetList.append(ord(a))
    
finalList = list(filter(lambda x : x > 40, map(ord, alphabetList)))

print([chr(a) for a in alphabetList])
# 왜안돼ㅠㅠ

"""
    [Q] 문자열 내부의 데이터를 검색하는 것과, 리스트 내부의 데이터를 검색하는 것 중 어떤 게 더 빠를까? :: 테스트 2가지 및 설명 :
        - ["A", "P", "P", "L", "E"]
        - "APPLE"
        문자열을 검색하는게 리스트에서 검색하는 것보다 빠름
        예제:
            import time

            alphabet = "abcdefghijklmnopqrstuvwxyz"
            alphabet_list = list(alphabet)

            # 문자열 검색
            start = time.time()
            "a" in alphabet
            end = time.time()
            print("문자열 검색:", end - start)

            # 리스트 검색
            start = time.time()
            "a" in alphabet_list
            end = time.time()
            print("리스트 검색:", end - start)
            
            
            # 예제2
            apple = "apple"
            appleList = ["a", "p", "p", "l", "e"]
            
            # 문자열 검색
            start = time.time()
            "a" in apple
            end = time.time()
            print("문자열 검색:", end - start)

            # 리스트 검색
            start = time.time()
            "a" in appleList
            end = time.time()
            print("리스트 검색:", end - start)

        
    [Q] 문자열과 리스트 중 어느 것이 데이터의 크기가 더 클까? : 
        - ["A", "P", "P", "L", "E"]
        - "APPLE"
        문자열은 불변하기에 각각 데이터를 쓰는 리스트보다 훨신 적은 데이터를 소비함
        심하면 10배 이상 차이날 수도 있음

"""

# 예제1
import time

num = "0123456789"
numList = list(num)

start = time.time()
"7" in num
end = time.time()
print("문자열:", end - start)

start = time.time()
"7" in numList
end = time.time()
print("리스트:", end - start)




"""
    [Q] 위 코드는 어떻게 동작하는 걸까? :: 각 부분별로 설명하고, 예제 하나 더 제시하기!
    - chars = '+_)(*&^%$#@!~)'
    # chars의 문자들에 ord(번호) 적용 후 40보다 큰 값만 필터링해 리스트로 묶음
    - code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
"""
# 예제
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numberList = list(filter(lambda z : z % 2 == 0, number))
print(numberList)


"""
    [Q] 메서드가 값을 return 할 때애도 2개 이상의 데이터를 return 할 수 있을까? :: 테스트 밑 예제 2가지
    파이선에서는 복수의 데이터를 반환하는 것이 가능하며, 실무에서도 많이 사용되는 기능임
    
    def func():
        return 1, 2, 3


    def get_user_info():
        name = "홍길동"
        age = 30
        return name, age

    info = get_user_info()
    print(info)          # ('홍길동', 30) → 튜플 반환
    print(info[0])       # '홍길동'
    
"""

class abc:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def ret(self):
        return self.a, self.b, self.c
    
abc = abc(1, 2 ,3)
print(abc.ret())

"""
    [Q] 만일 2개 이상의 데이터가 return 이 된다면, 그 반환값의 데이터 타입은 어떠할까? (List? Set? Tuple?) :: 테스트 및 예제 2가지
    위와 같은 상황이라면 기본적으로 튜플로 반환되나, 필요에 따라 딕셔너리, 리스트로도 반한이 가능함
    
    def get_data():
    if error_occurred:
        return False, "에러 발생"
    return True, {"id": 1, "name": "user"}

    def get_min_max(numbers):
    return min(numbers), max(numbers)

"""

def apple() :
    return 1, 2, 4

print(apple())


"""
    [Q] 불특정 다수의 데이터도 return 할 수 있을까? :: 설명, 테스트 및 예제 2가지!
        - return x, y, *rest
        - return *many
    파이선에서는 위와 같은 데이터들도 유연한 반환이 가능함
    
    def func():
        x = 1
        y = 2
        others = [3, 4, 5]
        return x, y, *others  # (*others가 풀려서 튜플로 들어감)

    print(func())  
    # 출력: (1, 2, 3, 4, 5)
    
    def func():
        many = [1, 2, 3]
        return *many     # ❌ SyntaxError

    # 하지만 이렇게 하면 됨
    def func():
        many = [1, 2, 3]
        return (*many,)  # ✅ 튜플로 감싸면 가능

    print(func())  # (1, 2, 3)

"""
def ac():
    
    color = ["yellow", "black", "red", "white"]
    return (*color,)

print(ac())


"""
    [Q] sorted 는 리스트만 정렬해주나? 아니면 여러가지 배열 데이터를 다 정렬 가능한가? :: 각 종류별 예제 2가지씩!
    sorted는 리스트 뿐만 아니라 딕셔너리, 문자열 등등 정렬이 가능
    
    scores = {"kim": 70, "lee": 90, "park": 80}

    # 키 기준
    sorted(scores)
    # ['kim', 'lee', 'park']

    # 값 기준
    sorted(scores.items(), key=lambda x: x[1], reverse=True)
    # [('lee', 90), ('park', 80), ('kim', 70)]
    
    
    s = "zxcvbnmasd"
    sorted(s)
    # ['a', 'b', 'c', 'd', 'm', 'n', 's', 'v', 'x', 'z']
    
"""

humanDict = {
    "name" : "Kim",
    "age" : 40,
    "gender" : "Men"
}

# dict.items : 딕셔너리의 모든 키와 밸류 쌍을 튜플로 반환
print(sorted(humanDict.items(), key=lambda x : x[0]))

"""
    [Q] sorted 의 결과물은 깊은 복사인가, 얕은 복사인가? :: 설명 및 예제 2가지
    기존의 값을 변경하는게 아닌 정렬된 새로운 값을 뱉기에 얕은 복사라 볼 수 있음
    깊은 복사로 사용하고 싶을 경우 deepcopy를 따로 해줘야함
    
    # 얕은 복사
    a = [[3, 4], [1, 2], [5, 6]]
    b = sorted(a)  # 얕은 복사

    print(a is b)         # False (다른 객체)
    print(a[0] is b[0])   # True (같은 내부 객체)

    # 깊은 복사로 활용
    import copy

    deep_copied = copy.deepcopy(sorted(a))

"""


"""
    [Q] 현업에서는 sorted 를 어떤 용도로 사용할끼? :: 설명 및 예제 2가지
    차순으로 정렬할 수 있다는 점을 이용해 상위/하위 값을 골라내거나 하는 등 값을 원하는 조건으로 정렬하는데 사용
    
    # 예시1 : 상위 n명
    users = [
    {"name": "kim", "score": 95},
    {"name": "lee", "score": 85},
    {"name": "park", "score": 92},
]

    # 점수 높은 순으로 정렬 후 상위 2명
    top_users = sorted(users, key=lambda x: x['score'], reverse=True)[:2]
    
    # 딕셔너리 값 정렬
    sales = {"A": 120, "B": 80, "C": 150}

    # 판매량 높은 순
    sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)
    # [('C', 150), ('A', 120), ('B', 80)]


"""