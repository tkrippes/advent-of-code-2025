from enum import Enum


class RotationDirection(Enum):
    """
    Enum representing rotation directions.
    """

    LEFT = 0
    RIGHT = 1


class Rotation:
    """
    Class representing a rotation with a direction (left or right)
    and distance.
    """

    def __init__(self, direction: RotationDirection, distance: int):
        self.direction = direction
        self.distance = distance

    def __repr__(self) -> str:
        return f"Rotation(direction={self.direction}, distance={self.distance})"
