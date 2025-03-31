
# 제네레이터 예제

# 일반 클래스
class GenG:
    # 생성자
    def __init__(self, text):
        self._idx = 0
        self._text = text.split('G')
    
    # G를 기준으로 문장 나누기
    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise Exception('error')
        self._idx += 1
        return word
    
# 인스턴스 생성
g1 = GenG("GenG is the best proGaminG team")

# 끊긴 부분만큼 G빼고 출력
print(g1)
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))


# 제네레이터 클래스
class GenGenG:
    def __init__(self, text):
        self._text = text.split('G')
        
    def __iter__(self):
        for word in self._text:
            # 제네레이터
            yield word
        # return 없어도 반환함
        return 
    
    def __repr__(self):
        return 'GenGenG(%s)' % (self._text)

# 인스턴스 생성
g2 = GenGenG("GenG is the best proGaminG team")

# 이터레이터 객체로 변환?(안하면 큰일남;;)
wt = iter(g2)

# 끊긴 부분만큼 G빼고 출력
print(wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
