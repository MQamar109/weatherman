import parser

from handlers import (print_year_result,
                      print_month_average_results,
                      print_combine_graph,
                      print_separate_graph)

if __name__ == '__main__':
    args = parser.get_parser()

    if args.year:
        print_year_result(args.path, args.year)

    if args.month:
        print_month_average_results(args.path, args.month)

    if args.graph:
        print_separate_graph(args.path, args.graph)

    if args.combine_graph:
        print_combine_graph(args.path, args.combine_graph)
