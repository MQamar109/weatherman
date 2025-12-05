import argparse

def get_parser():
    parser = argparse.ArgumentParser(prog="Weather man", description="Find out the command type.")
    parser.add_argument('path', help='Path of the folder of all the files of weatherman.')
    parser.add_argument('-e', '--year', help="Take the year", type=int)
    parser.add_argument('-a', '--month', help='Take Year with month like:2000/06')
    parser.add_argument('-c', '--graph', help='Take year and month and generate report on 2 lines')
    parser.add_argument('-p', '--combine-graph', help='Take year and month and generate report on 1 line')
    return parser.parse_args()
