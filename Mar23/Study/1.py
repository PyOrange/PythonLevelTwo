

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

# 딕셔너리 
del waterDict[1]



