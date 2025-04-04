
# 이터레이터, 제네레이터

# 이터레이터 : 반복 가능한 객체
# 제네레이터 : 이터레이터를 생성하는 방법 중 하나

# 파이선 반복 가능한 타입
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 반복 가능한 이유 :  iter(t) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for 반복문으로 t의 단어 한 글자씩 출력
for c in t:
    print(c)

print()

# while 반복
# 이터레이터 생성
w = iter(t)

# 이터레이터 이용한 반복문으로 t의 단어 한 글자씩 출력
while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# abc : 추상 베이스 클래스, 리스트, 딕셔너리, 세트 등이 특정 메서드를 포함하고 있는지 확인하거나 커스텀 클래스를 만들 때 유용합니다.
from collections import abc

# 반복 가능한 객체인지 확인
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()
print()

# 클래스로 구현
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        # 공백을 기준으로 나눔
        self._text = text.split(' ')
    
    # 문장을 특정 단어를 기준으로 나누어 반환
    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tomorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()

# 제네레이터 형태의 장점
# 1.지능형 리스트, 딕셔너리, 집합 : 데이터 양 증가 : 메모리 사용량 증가 : 제네레이터 권장
# 2.단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3.작은 메모리 조각 사용

# 위 클래스를 제네레이터 형태로
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        # print('Called __iter__')
        for word in self._text:
            # 제네레이터
            yield word 
        return # 없어도 됨
    
    def __repr__(self):
        return 'WordSplitGenerator(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)

print(wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

print()
print()