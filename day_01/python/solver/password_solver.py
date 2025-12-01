from ..rotation import Rotation, RotationDirection


def solve_password_part_1(rotations: list[Rotation]) -> int:
    """
    Solve password based on the list of rotations and dial start position 50.

    The password is determined by the number of time the dial is pointing
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

        # reset dial position in range 0-99
        current_dial_position %= 100
        if current_dial_position == 0:
            password += 1

    return password


def solve_password_part_2(rotations: list[Rotation]) -> int:
    """
    Solve password based on the list of rotations and dial start position 50.

    The password is determined by the number of time the dial is pointing
    to 0 at any time.
    """
    min_dial_position: int = 0
    max_dial_position: int = 99
    dial_start_position: int = 50
    current_dial_position: int = dial_start_position
    last_dial_position: int = dial_start_position
    password: int = 0

    for rotation in rotations:
        last_dial_position = current_dial_position

        if rotation.direction == RotationDirection.LEFT:
            current_dial_position -= rotation.distance

            # add one for each time the dial crosses 0
            while current_dial_position < min_dial_position:
                current_dial_position += max_dial_position + 1
                password += 1

            # add one if dial points exactly on 0
            if current_dial_position == min_dial_position:
                password += 1

            # substract one if dial started on 0 (no crossing)
            if last_dial_position == min_dial_position:
                password -= 1
        elif rotation.direction == RotationDirection.RIGHT:
            current_dial_position += rotation.distance

            while current_dial_position > max_dial_position:
                current_dial_position -= max_dial_position + 1
                password += 1
        else:
            raise ValueError(f"Unhandled rotation direction: {rotation.direction}")

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

    print(
        f"Password for test rotations (part 1): {solve_password_part_1(test_rotations)}"
    )
    print(
        f"Password for test rotations (part 2): {solve_password_part_2(test_rotations)}"
    )
