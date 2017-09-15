import main
import use_termext
import sys


def main(keyword, page):
    main.main(keyword, page)
    use_termext.main()


if __name__ == '__main__':
    keyword = sys.argv[1]
    page = sys.argv[2]
    main(keyword, page)
