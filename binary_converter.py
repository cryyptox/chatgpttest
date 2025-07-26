# binary_converter.py
"""Simple script to convert a given number to its binary representation."""

import sys


def to_binary(number: int) -> str:
    """Return the binary representation of ``number`` as a string."""
    return bin(number)


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <number>")
        raise SystemExit(1)
    try:
        value = int(argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        raise SystemExit(1)

    print(to_binary(value))


if __name__ == "__main__":
    main(sys.argv)
