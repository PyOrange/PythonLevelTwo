

# 기존의 리스트
chars = '+_)(*&^%$#@!~)'
code_list1 = []

for s in chars:
    # 유니코드를 담아놓은 리스트
    code_list1.append(ord(s))
    
"""
    [Q] 문자열 내부의 데이터를 검색하는 것과, 리스트 내부의 데이터를 검색하는 것 중 어떤 게 더 빠를까? :: 테스트 2가지 및 설명
        - ["A", "P", "P", "L", "E"]
        - "APPLE"
        
    [Q] 문자열과 리스트 중 어느 것이 데이터의 크기가 더 클까?
        - ["A", "P", "P", "L", "E"]
        - "APPLE"
        
"""

# 지능형 리스트 : 기존의 리스트보다 더 간단하게 생성 및 활용 가능
code_list2 = [ord(s) for s in chars]


# 아래가 속도가 조금 더 빠름
code_list3 = [ord(s) for s in chars if ord(s) > 40]

# filter는 함수와 자료구조형 데이터를 받음
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

"""
    [Q] 위 코드는 어떻게 동작하는 걸까? :: 각 부분별로 설명하고, 예제 하나 더 제시하기!
    - chars = '+_)(*&^%$#@!~)'
    - code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))
"""

# 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()




