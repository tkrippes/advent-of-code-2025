from ..rotation import Rotation, RotationDirection


def solve_password(rotations: list[Rotation]) -> int:
    """
    Solve password based on the list of rotations and dial start position 50.

    The password is determinec by the number of time the dial is pointing
    to 0 after any rotation.
    """
    dial_start_position: int = 50
    current_dial_position: int = dial_start_position
    password: int = 0

    for rotation in rotations:
        if rotation.direction == RotationDirection.LEFT:
            current_dial_position -= rotation.distance
        elif rotation.direction == RotationDirection.RIGHT:
            current_dial_position += rotation.distance
        else:
            raise ValueError(f"Unhandled rotation direction: {rotation.direction}")

        # set dial position in range 0-99
        current_dial_position %= 100
        if current_dial_position == 0:
            password += 1

    return password


if __name__ == "__main__":
    # test example
    test_rotations: list[Rotation] = [
        Rotation(RotationDirection.LEFT, 68),
        Rotation(RotationDirection.LEFT, 30),
        Rotation(RotationDirection.RIGHT, 48),
        Rotation(RotationDirection.LEFT, 5),
        Rotation(RotationDirection.RIGHT, 60),
        Rotation(RotationDirection.LEFT, 55),
        Rotation(RotationDirection.LEFT, 1),
        Rotation(RotationDirection.LEFT, 99),
        Rotation(RotationDirection.RIGHT, 14),
        Rotation(RotationDirection.LEFT, 82),
    ]

    print(f"Password for test rotations: {solve_password(test_rotations)}")
