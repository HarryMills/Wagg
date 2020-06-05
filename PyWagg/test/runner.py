import unittest
import os


def main():
    load = unittest.TestLoader()

    cur_path = os.path.dirname(os.path.dirname(__file__))
    suite = load.discover(cur_path, "*_test.py")

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == '__main__':
    main()
