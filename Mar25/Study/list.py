

# 기존의 리스트
chars = '+_)(*&^%$#@!~)'
code_list1 = []

for s in chars:
    # 유니코드를 담아놓은 리스트
    code_list1.append(ord(s))

# 지능형 리스트 : 기존의 리스트보다 더 간단하게 생성 및 활용 가능
code_list2 = [ord(s) for s in chars]

# 아래가 속도가 조금 더 빠름
code_list3 = [ord(s) for s in chars if ord(s) > 40]
# filter는 함수와 자료구조형 데이터를 받음
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

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




