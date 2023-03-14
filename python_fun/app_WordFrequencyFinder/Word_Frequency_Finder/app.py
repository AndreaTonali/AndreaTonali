from helper import parser, frequency
from config import TEXT_FILE


def main() -> None:

    data = parser(TEXT_FILE)

    for key, size in sorted(frequency(data).items()):
        print(('{}: {}'.format(key, int(size) * '*')))


if __name__ == '__main__':
    main()
