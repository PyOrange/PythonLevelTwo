# Chapter04-04
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict
from types import MappingProxyType

d = {'k': 'v'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['k'] = 'v2'

d['k2'] = 'v2'

print(d)

print()
print()

s1 = {'a', 'b', 'c'}
s2 = set(['a', 'b', 'a'])
s3 = {3}
s4 = set() # {}로 선언하면 안됨
s5 = frozenset({'a', 'b', 'a'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
from dis import dis

print('------')
print(dis('{10}'))

print('------')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

print('------')

print({name(chr(i), '') for i in range(0,256)})