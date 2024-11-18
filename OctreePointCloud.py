# Thomas Safago
# 11/17/2024


from AbstractPointCloud import AbstractPointCloud
from Point import Point
from PointMethods import get_distance


class AABB:
    # Attributes
    min = None
    max = None

    # Init
    def __init__(self, min, max):
        self.min = min
        self.max = max

    # Helpers
    def inside(self, point):
        return (
            self.min.x <= point.x <= self.max.x and
            self.min.y <= point.y <= self.max.y and
            self.min.z <= point.z <= self.max.z
        )

    def center(self):
        return Point(
            (self.max.x + self.min.x) / 2,
            (self.max.y + self.min.y) / 2,
            (self.max.z + self.min.z) / 2
        )

    def within_radius(self, point, radius):
        closest_point = Point(
            max(self.min.x, min(point.x, self.max.x)),
            max(self.min.y, min(point.y, self.max.y)),
            max(self.min.z, min(point.z, self.max.z))
        )

        return get_distance(closest_point, point) <= radius


class OctreeNode:
    # Attributes
    aabb = None
    points = []
    octants = [None] * 8
    max_points = 32
    depth = 12

    # Init
    def __init__(self, aabb, depth=8):
        self.aabb = aabb
        self.depth = depth
        self.points = []

    def is_leaf(self):
        return self.octants[0] is None

    def subdivide(self):
        center = self.aabb.center()

        self.octants = [
            AABB(self.aabb.min, center),
            AABB(Point(center.x, self.aabb.min.y, self.aabb.min.z), Point(self.aabb.max.x, center.y, center.z)),
            AABB(Point(self.aabb.min.x, center.y, self.aabb.min.z), Point(center.x, self.aabb.max.y, center.z)),
            AABB(Point(center.x, center.y, self.aabb.min.z), Point(self.aabb.max.x, self.aabb.max.y, center.z)),
            AABB(Point(self.aabb.min.x, self.aabb.min.y, center.z), Point(center.x, center.y, self.aabb.max.z)),
            AABB(Point(center.x, self.aabb.min.y, center.z), Point(self.aabb.max.x, center.y, self.aabb.max.z)),
            AABB(Point(self.aabb.min.x, center.y, center.z), Point(center.x, self.aabb.max.y, self.aabb.max.z)),
            AABB(center, self.aabb.max)
        ]

        for i, octant in enumerate(self.octants):
            self.octants[i] = OctreeNode(octant, self.depth - 1)

    def fill(self, points):
        self.points = points

        if self.depth <= 0:
            return False

        if len(points) > self.max_points:
            self.subdivide()

            for point in points:
                for octant in self.octants:
                    if octant.aabb.inside(point):
                        octant.points.append(point)
                        break

            for octant in self.octants:
                octant.fill(octant.points)

            self.points = []

        return True  # Successful fill

    def radius_search(self, point, radius, points):
        if not self.aabb.within_radius(point, radius):
            return False

        for p in self.points:
            if get_distance(p, point) <= radius:
                points.append(p)

        if not self.is_leaf():
            for octant in self.octants:
                octant.radius_search(point, radius, points)


class OctreePointCloud(AbstractPointCloud):
    # Attributes
    root = None

    # Init
    def __init__(self, points_list):
        self.root = OctreeNode(AABB(Point(-1, -1, -1), Point(1, 1, 1)))
        self.build_acceleration_structure(points_list)

    # Methods
    def build_acceleration_structure(self, points_list):
        self.root.fill(points_list)

    def radius_search(self, point, radius):
        points = []
        self.root.radius_search(point, radius, points)
        return points
