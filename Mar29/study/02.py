
# 제네레이터 Ex1
def generator_ex1():
    print('Start')
    yield 'A Point.'
    print('continue')
    yield 'B Point.'
    print('End')

temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

print()

# 제네레이터 Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

print()
print()

for i in temp3:
    print(i)

print()
print()


# 제네레이터 Ex3(중요 함수 만들기)
# 중요 함수 : filterfalse, accumulate, chain, product, product, groupby
import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

print()

# takewhile : 조건을 활용한 반복
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print(v)


print()

# filterfalse : 조건에 반대되는 값 반환
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)


print()

# 누적된 합
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

print()

# 앞 객체와 뒤 객의 값을 연결
gen5 = itertools.chain('ABCDE', range(1,11,2))

print(list(gen5))

# 연결2
# enumerate : 데이터 앞에 키값으로 인덱스 번호 달아줌
gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')

print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)

print(list(gen8))

# groupby : 이터레이터를 그룹화?
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group))

print()