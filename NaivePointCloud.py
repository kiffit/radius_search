# Thomas Safago
# 11/17/2024


from AbstractPointCloud import AbstractPointCloud
from PointMethods import get_distance


class NaivePointCloud(AbstractPointCloud):
    # Attributes
    points_list = []

    # Init
    def __init__(self, points_list):
        self.build_acceleration_structure(points_list)

    # Helpers
    def build_acceleration_structure(self, points_list):
        self.points_list = points_list

    def radius_search(self, point, radius):
        result = []

        for p in self.points_list:
            if get_distance(point, p) <= radius:
                result.append(p)

        return result
