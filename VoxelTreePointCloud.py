# Isac Portillo
# 12/15/2024


from AbstractPointCloud import AbstractPointCloud
from OctreePointCloud import AABB
from Point import Point
from PointMethods import get_distance_squared


class VoxelTreeNode:
    # Instance Variables
    aabb = None
    points = []

    # Constructor
    def __init__(self, aabb):
        self.aabb = aabb
        self.points = []

    # Methods
    def contains_point(self, point):
        return self.aabb.inside(point)


class VoxelTreePointCloud(AbstractPointCloud):
    # Attributes
    voxel_size = None  # Assume square voxels. Can possibly cover more space than needed
    voxels = {}

    # Init
    def __init__(self, points_list, voxel_size):
        self.voxel_size = voxel_size
        self.build_acceleration_structure(points_list)

    # Helpers
    def __voxel_index(self, point):
        return point.x // self.voxel_size, point.y // self.voxel_size, point.z // self.voxel_size

    def __search_bounds(self, center, radius):
        radius_point = Point(radius, radius, radius)
        min_index = self.__voxel_index(center - radius_point)
        max_index = self.__voxel_index(center + radius_point)
        return min_index, max_index

    def build_acceleration_structure(self, points_list):
        for point in points_list:
            index = self.__voxel_index(point)
            if index not in self.voxels:
                min_corner = Point(index[0] * self.voxel_size, index[1] * self.voxel_size, index[2] * self.voxel_size)
                max_corner = min_corner + Point(self.voxel_size, self.voxel_size, self.voxel_size)
                self.voxels[index] = VoxelTreeNode(AABB(min_corner, max_corner))
            self.voxels[index].points.append(point)

    def radius_search(self, point, radius):
        min, max = self.__search_bounds(point, radius)
        rough_points = []

        for x in range(int(min[0]), int(max[0]) + 1):
            for y in range(int(min[1]), int(max[1]) + 1):
                for z in range(int(min[2]), int(max[2]) + 1):
                    index = (x, y, z)
                    if index in self.voxels:
                        node = self.voxels[index]
                        if node.aabb.within_radius(point, radius):
                            rough_points.extend(node.points)

        exact_points = []

        for test_point in rough_points:
            if get_distance_squared(point, test_point) <= radius ** 2:
                exact_points.append(point)

        return exact_points
