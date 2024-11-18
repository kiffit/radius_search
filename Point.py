# Thomas Safago
# 11/17/2024


class Point:
    # Attributes
    x = None
    y = None
    z = None

    # Init
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Helpers
    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z
        return None

    # To string
    def __str__(self):
        return (
            f"Point:"
            f"\n\tx: {self.x}"
            f"\n\ty: {self.y}"
            f"\n\tz: {self.z}"
        )



