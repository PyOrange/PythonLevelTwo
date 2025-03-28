

# 지능형 리스트 실습

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetList = []

for a in alphabetList:
    alphabetList.append(ord(a))
    
finalList = list(filter(lambda x : x > 40, map(ord, alphabetList)))

print([chr(a) for a in alphabetList])
# 왜안돼ㅠㅠ