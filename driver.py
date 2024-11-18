# Thomas Safago
# 11/17/2024


from Point import Point
from KDTreePointCloud import KDTreePointCloud
from NaivePointCloud import NaivePointCloud
from OctreePointCloud import OctreePointCloud
from PointMethods import get_distance

from random import uniform
import time


def main():
    points_amount = 1000000
    radius = .1
    points_list = [None] * points_amount

    for i in range(points_amount):
        points_list[i] = Point(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))

    print("\nStarting KD-Tree Point Cloud construction...")
    st = time.time()
    kdpc1 = KDTreePointCloud(points_list)
    et = time.time()
    print(f"KD-Tree construction finished in {et-st} seconds.")

    print("\nStarting Octree Point Cloud construction...")
    st = time.time()
    octpc1 = OctreePointCloud(points_list)
    et = time.time()
    print(f"Octree construction finished in {et - st} seconds.")

    npc1 = NaivePointCloud(points_list)

    print(f"\nStarting r={radius} search on KD-Tree Point Cloud (n={points_amount})...")
    st = time.time()
    kdpc1.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"Search finished! Time elapsed: {et-st} seconds.")

    print(f"\nStarting r={radius} search on Octree Point Cloud (n={points_amount})...")
    st = time.time()
    octpc1.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"Search finished! Time elapsed: {et - st} seconds.")

    print(f"\nStarting r={radius} search on Naive Point Cloud (n={points_amount})...")
    st = time.time()
    npc1.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"Search finished! Time elapsed: {et-st} seconds.")


if __name__ == '__main__':
    main()
