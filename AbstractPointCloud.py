# Thomas Safago
# 11/17/2024


"""
Some important notes about point clouds rest here.
There are no insert points methods because a points list is the most basic form of a point cloud.
If points must be added or removed, for the sake of efficiency the entire acceleration structure should be rebuilt.
An imbalanced structure will result in highly inefficient lookups and defeat the purpose of such a structure.
The cost is allocated in the generation of the structure. The static structure will excel in performance of lookups.
"""


from abc import abstractmethod


class AbstractPointCloud:
    # Init
    @abstractmethod
    def __init__(self, points_list):
        pass

    # Helpers
    @abstractmethod
    def build_acceleration_structure(self, points_list):
        pass

    @abstractmethod
    def radius_search(self, point, radius):
        pass
