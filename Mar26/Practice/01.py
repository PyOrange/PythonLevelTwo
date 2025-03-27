
# 일급 함수 실습
# 팩토리얼 메서드 구현
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# 팩토리얼 메서드를 활용한 순열 구현
def permutation(n, r):
    return factorial(n) // factorial(n - r)

# 팩토리얼 함수 정의
func = factorial

# map, filter 활용해 함수 사용
print(list(map(func, filter(lambda x : x % 2, range(1, 20)))))
