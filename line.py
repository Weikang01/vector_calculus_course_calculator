from vector import Vec3


class Line:
    @staticmethod
    def line(v1, v2):
        direction = v2 - v1
        return Line(v1, direction)

    def __init__(self, origin: Vec3, direction: Vec3):
        self.origin = origin
        self.direction = direction

    def expanded_formula(self):
        return f"x = {self.origin.x} + {self.direction.x}t\n"\
               f"y = {self.origin.y} + {self.direction.y}t\n"\
               f"z = {self.origin.z} + {self.direction.z}t\n"

    def point_on_line(self, t) -> Vec3:
        return Vec3(self.origin.x + self.direction.x * t,
                    self.origin.y + self.direction.y * t,
                    self.origin.z + self.direction.z * t)

    def __str__(self):
        return f"{self.origin} + {self.direction}t"
