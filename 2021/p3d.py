import typing


class P(typing.NamedTuple):
    x: int
    y: int
    z: int

    def rotations(self, n: int) -> "P":
        x, y, z = self
        rots = [
            # positive z up
            (-x, -y, +z),
            (-y, +x, +z),
            (+x, +y, +z),
            (+y, -x, +z),
            # negative z up
            (+x, -y, -z),
            (-y, -x, -z),
            (-x, +y, -z),
            (+y, +x, -z),
            # positive x up
            (+y, +z, +x),
            (+z, -y, +x),
            (-y, -z, +x),
            (-z, +y, +x),
            # negative x up
            (-z, -y, -x),
            (-y, +z, -x),
            (+z, +y, -x),
            (+y, -z, -x),
            # positive y up
            (-z, -x, +y),
            (-x, +z, +y),
            (+z, +x, +y),
            (+x, -z, +y),
            # negative y up
            (+z, -x, -y),
            (-x, -z, -y),
            (-z, +x, -y),
            (+x, +z, -y),
        ]

        return P(*rots[n])

    def translate(self, vector: "P") -> "P":
        return P(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def sub(self, vector: "P") -> "P":
        return P(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def manhattan_distance(self, o: "P") -> int:
        diff = o.sub(self)
        return sum(map(abs, diff))
