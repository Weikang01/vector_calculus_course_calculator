from vector import Vec3


class Plane:
    @staticmethod
    def plane(v1: Vec3, v2: Vec3, v3: Vec3):
        ab = v2 - v1
        ac = v3 - v1
        normal = Vec3.cross(ab, ac)
        d = normal.x * v1.x + normal.y * v1.y + normal.z * v1.z
        print(
            f"AB = {ab}\nAC = {ac}\nnormal = ABxAC = {normal}\nequation: {normal.x}x + {normal.y}y + {normal.z}z = {d}")
        return Plane(normal.x, normal.y, normal.z, d)

    def __init__(self, x=0.0, y=0.0, z=0.0, d=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    def __str__(self):
        return f"{self.x}x + {self.y}y + {self.z}z = {self.d}"
