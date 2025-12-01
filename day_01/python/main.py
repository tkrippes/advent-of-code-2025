import os

from .rotation import Rotation
from .parser.rotations_parser import parse_rotations
from .solver.password_solver import solve_password


def part_1() -> int:
    """
    Solve part 1 of day 1."""
    input_file_name: str = os.path.join(
        os.path.dirname(__file__),
        "..",
        "input",
        "input.txt",
    )
    rotations: list[Rotation] = parse_rotations(input_file_name)

    return solve_password(rotations)


if __name__ == "__main__":
    print(f"Result of part 1: {part_1()}")
