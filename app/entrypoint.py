"""
The entry point of the Python Wheel
"""
import os
import sys
import argparse
import SparkTest
from behave import __main__

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument("-s", "--script", help="Python file to run")


def main(argv=sys.argv[1:]):
    print('Entrypoint arguments:')
    print(sys.argv)
    print('CWD: ', os.getcwd())

    args = parser.parse_args(argv)
    if args.script:
        if args.script == 'SparkTest.py':
            print("Running SparkTest")
            SparkTest.run_query()
    else:
        __main__.main(args=argv)

    # This method will print the provided arguments


if __name__ == '__main__':
    main()
