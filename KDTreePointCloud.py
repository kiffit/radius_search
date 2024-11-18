# Thomas Safago
# 11/17/2024


from AbstractPointCloud import AbstractPointCloud
from PointMethods import get_distance


# KD Tree Node
class KDTreeNode:
    # Attributes
    value = None
    left = None
    right = None

    # Init
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# KD Tree
class KDTreePointCloud(AbstractPointCloud):
    # Attributes
    root = None

    # Init
    def __init__(self, points_list):
        self.build_acceleration_structure(points_list)

    # Helpers
    def build_acceleration_structure(self, points_list):
        if len(points_list) == 0:
            self.root = None
        else:
            self.root = self._build_acceleration_structure(points_list)

    def _build_acceleration_structure(self, points, depth=0):
        # Is a leaf
        if len(points) == 0:
            return None

        points.sort(key=lambda x: x[depth % 3])  # Sort by axis based on depth

        median_index = len(points) // 2
        median_point = points[median_index]

        left = self._build_acceleration_structure(points[:median_index], depth + 1)  # Evan gave idea for list slicing
        right = self._build_acceleration_structure(points[median_index + 1:], depth + 1)

        return KDTreeNode(median_point, left, right)

    def radius_search(self, point, radius):
        points = []
        self._radius_search(self.root, point, radius, points)
        return points

    def _radius_search(self, node, point, radius, points, depth=0):
        if node is None:
            return None

        if get_distance(node.value, point) <= radius:
            points.append(node.value)

        axis = depth % 3

        if point[axis] < node.value[axis]:
            self._radius_search(node.left, point, radius, points, depth + 1)
            if abs(point[axis] - node.value[axis]) <= radius:
                self._radius_search(node.right, point, radius, points, depth + 1)
        else:
            self._radius_search(node.right, point, radius, points, depth + 1)
            if abs(point[axis] - node.value[axis]) <= radius:
                self._radius_search(node.left, point, radius, points, depth + 1)
