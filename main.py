from line import Line, Vec3
from plane import Plane
from matrix import Matrix


def intersect(plane: Plane, line: Line):
    deno = line.direction.x * plane.x + \
           line.direction.y * plane.y + \
           line.direction.z * plane.z
    nume = plane.d - \
           line.origin.x * plane.x - \
           line.origin.y * plane.y - \
           line.origin.z * plane.z
    if deno == 0:
        if nume == 0:
            return "line is on the plane"
        else:
            return "line is parallel to the plane"
    t = nume / deno
    r = line.point_on_line(t)
    return f"{'are orthogonal' if Vec3.are_parallel(Vec3(plane.x, plane.y, plane.z), line.direction) else 'not orthogonal'}\nt = {t}\npoint is: {r}"


if __name__ == '__main__':
    m = Matrix.matrix([
        [3, 2, 3],
        [-2, -3, -2],
        [-1, 3, -1]
    ])

    print(m.det())
