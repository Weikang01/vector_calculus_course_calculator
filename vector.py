import math


class Vec3:
    @staticmethod
    def midpoint(v1, v2):
        return Vec3((v1.x + v2.x) * .5, (v1.y + v2.y) * .5, (v1.z + v2.z) * .5)

    @staticmethod
    def dot(v1, v2) -> float:
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1, v2):
        return Vec3(v1.y * v2.z - v1.z * v2.y,
                    v1.z * v2.x - v1.x * v2.z,
                    v1.x * v2.y - v1.y * v2.x)

    @staticmethod
    def length(v):
        return math.sqrt(Vec3.dot(v, v))

    @staticmethod
    def normalize(v):
        return v / Vec3.length(v)

    @staticmethod
    def are_parallel(v1, v2) -> bool:
        rate = v1.x / v2.x
        if rate * v2.y != v1.y:
            return False
        if rate * v2.z != v1.z:
            return False
        return True

    @staticmethod
    def are_orthogonal(v1, v2) -> bool:
        return Vec3.dot(v1, v2) == 0

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif type(other) == int or type(other) == float:
            return Vec3(self.x + other, self.y + other, self.z + other)
        else:
            print("Not a valid data type!")
            return None

    def __iadd__(self, other):
        if type(other) == Vec3:
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        elif type(other) == int or type(other) == float:
            self.x += other
            self.y += other
            self.z += other
            return self
        else:
            print("Not a valid data type!")
            return None

    def __sub__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif type(other) == int or type(other) == float:
            return Vec3(self.x - other, self.y - other, self.z - other)
        else:
            print("Not a valid data type!")
            return None

    def __isub__(self, other):
        if type(other) == Vec3:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        elif type(other) == int or type(other) == float:
            self.x -= other
            self.y -= other
            self.z -= other
            return self
        else:
            print("Not a valid data type!")
            return None

    def __mul__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == int or type(other) == float:
            return Vec3(self.x * other, self.y * other, self.z * other)
        else:
            print("Not a valid data type!")
            return None

    def __imul__(self, other):
        if type(other) == Vec3:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
            return self
        elif type(other) == int or type(other) == float:
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        else:
            print("Not a valid data type!")
            return None

    def __truediv__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif type(other) == int or type(other) == float:
            return Vec3(self.x / other, self.y / other, self.z / other)
        else:
            print("Not a valid data type!")
            return None

    def __floordiv__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x // other.x, self.y // other.y, self.z // other.z)
        elif type(other) == int or type(other) == float:
            return Vec3(self.x // other, self.y // other, self.z // other)
        else:
            print("Not a valid data type!")
            return None

    def __eq__(self, other):
        if type(other) != Vec3:
            return False
        else:
            return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        if type(other) != Vec3:
            return True
        else:
            return self.x != other.x or self.y != other.y or self.z != other.z

    def __abs__(self):
        return Vec3(abs(self.x), abs(self.y), abs(self.z))

    def __str__(self):
        return f"< {self.x}, {self.y}, {self.z} >"

    def parallel_with(self, v2) -> bool:
        return Vec3.are_parallel(self, v2)

    def orthogonal_with(self, v2) -> bool:
        return Vec3.are_orthogonal(self, v2)

    def relation_with(self, v2):
        if self.orthogonal_with(v2):
            return "orthogonal"
        elif self.parallel_with(v2):
            return "parallel"
        else:
            return "others"
