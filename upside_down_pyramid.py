#!/usr/bin/env python3
import sys

def print_upside_down_pyramid(n: int) -> None:
    for i in range(n, 0, -1):
        spaces = n - i
        stars = 2 * i - 1
        print(' ' * spaces + '*' * stars)


def main() -> None:
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            if n < 1:
                raise ValueError
        except ValueError:
            print('Usage: python upside_down_pyramid.py [height>=1]')
            sys.exit(1)
    else:
        n = 5
    print_upside_down_pyramid(n)


if __name__ == '__main__':
    main()
