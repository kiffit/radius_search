# Thomas Safago
# 11/17/2024


from Point import Point
from KDTreePointCloud import KDTreePointCloud
from NaivePointCloud import NaivePointCloud
from OctreePointCloud import OctreePointCloud
from VoxelTreePointCloud import VoxelTreePointCloud
from math import pi
from random import uniform
import time


def main():
    # This function will generate all test cases and outputs
    run_tests()


def generate_points(points_amount):
    return [Point(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)) for _ in range(points_amount)]


def construct_point_clouds(points_list):
    print(f"=> BEGINNING POINT CLOUD CONSTRUCTION WITH {len(points_list)} POINTS")

    st = time.time()
    npc = NaivePointCloud(points_list)
    et = time.time()
    print(f"Naive tree construction finished in {et - st} seconds. (BASE CASE)")

    st = time.time()
    vtpc = VoxelTreePointCloud(points_list, 0.1)  # Voxel size optimized for this set
    et = time.time()
    print(f"Voxel tree construction finished in {et - st} seconds.")

    st = time.time()
    kdpc = KDTreePointCloud(points_list)
    et = time.time()
    print(f"KD-Tree construction finished in {et - st} seconds.")

    st = time.time()
    octpc = OctreePointCloud(points_list)
    et = time.time()
    print(f"Octree construction finished in {et - st} seconds.")

    return npc, vtpc, kdpc, octpc


def test_point_clouds(npc, vtpc, kdpc, octpc, radius):
    print(f"\t-> BEGINNING RADIUS SEARCH r={radius} (search coverage: {round((4/3)*pi*radius**3/8*100, 3)}%)")

    st = time.time()
    npc.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"\tNaive tree time: {et - st} seconds. (BASE CASE)")

    st = time.time()
    vtpc.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"\tVoxel tree time: {et - st} seconds.")

    st = time.time()
    kdpc.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"\tKD-Tree search time: {et-st} seconds.")

    st = time.time()
    octpc.radius_search(Point(0, 0, 0), radius)
    et = time.time()
    print(f"\tOctree search time: {et - st} seconds.")


def run_tests():
    test_point_counts = [10000, 100000, 1000000]
    test_radius_counts = [0.1, 0.5, 1]

    for points_amount in test_point_counts:
        print()
        npc, vtpc, kdpc, octpc = construct_point_clouds(generate_points(points_amount))
        print()
        for radius in test_radius_counts:
            test_point_clouds(npc, vtpc, kdpc, octpc, radius)
            print()

if __name__ == '__main__':
    main()
