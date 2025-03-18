class Vec:
    def __init__(self, *args):
        """
        벡터를 만드는 클래스
        """
        if len(args) == 0:
            self.x, self.y = 0, 0
        else : 
            self.x, self.y = args
            
    # 벡터 정보 반환
    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)
    
    # 벡터 뺄셈
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    # 벡터 나눗셈
    def __truediv__(self, other):
        return Vec(self.x / other.x, self.y / other.y)
    
    # 벡터 최솟값 반환
    def __bool__(self): 
        return bool(min(self.x, self.y))
    
# vec1 = Vec(1) # 에러;;
vec2 = Vec(41, 32)
vec3 = Vec(1, -1)
vec4 = Vec(0, 0)

# print(vec1) # 에러;;
print(vec2 - vec3) # Vector(40, 33)
# print(vec3 / vec4) # 에러;;
print(vec2 / vec3) # Vector(41.0, -32.0)
print(bool(vec3)) # True


