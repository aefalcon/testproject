"Test project"
import sys
import logging


def main() -> int:
    "entry point"
    logging.basicConfig(level=logging.INFO)
    return 0


if __name__ == '__main__':
    sys.exit(main())
