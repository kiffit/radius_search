# Thomas Safago
# 11/17/2024


"""
This class provides methods for working with points/lists of points.
"""


from math import sqrt


# Sorting by axis
def sort_x(points):
    return sorted(points, key=lambda x: x[0])  # Sort and retrieve ordered list based on x coordinates


def sort_y(points):
    return sorted(points, key=lambda x: x[1])  # Sort and retrieve ordered list based on x coordinates


def sort_z(points):
    return sorted(points, key=lambda x: x[2])  # Sort and retrieve ordered list based on x coordinates


def sort_axis(points, axis):
    return sorted(points, key=lambda x: x[axis])  # For use with integer axis, when axis isn't known prior

# Median
def get_median_index(points):
    return len(points) // 2


def get_median_point(points):  # Median really only works on sorted lists
    return points[get_median_index(points)]

# Distance
def get_distance_squared(point1, point2):
    return pow(point2[0] - point1[0], 2) + pow(point2[1] - point1[1], 2) + pow(point2[2] - point1[2], 2)

def get_distance(point1, point2):
    return sqrt(get_distance_squared(point1, point2))
