import os

from ..rotation import Rotation, RotationDirection


def parse_rotations(input_file_name: str) -> list[Rotation]:
    """
    Parse rotations list from input file.
    """
    with open(input_file_name, "r", encoding="utf-8") as file:
        rotations: list[Rotation] = []
        lines = file.readlines()

        for line in lines:
            direction: str = line[0]
            if direction not in ["L", "R"]:
                raise ValueError(f"Invalid rotation direction: {direction}")

            try:
                distance: int = int(line[1:].strip())
            except ValueError as e:
                raise ValueError(
                    f"Invalid rotation distance: {line[1:].strip()}"
                ) from e

            if direction == "L":
                rotations.append(Rotation(RotationDirection.LEFT, distance))
            elif direction == "R":
                rotations.append(Rotation(RotationDirection.RIGHT, distance))
            else:
                raise ValueError(f"Unhandled rotation direction: {direction}")

        return rotations


if __name__ == "__main__":
    # test example
    test_file_name: str = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "input",
        "test_input.txt",
    )

    print(f"Result of test input: {parse_rotations(test_file_name)}")
