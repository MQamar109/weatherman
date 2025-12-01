# This is a sample Python script.
import parser
from handlers import print_graph_separate_lines,print_graph_single_line,get_year_calculations_and_date,calculate_month_averages


if __name__ == '__main__':
    args=parser.get_parser()
    if args.year:
        get_year_calculations_and_date(args.path, args.year)
    if args.month:
        calculate_month_averages(args.path,args.month)
    if args.separate_graph:
        print_graph_separate_lines(args.path,args.separate_graph)
    if args.graph:
        print_graph_single_line(args.path,args.graph)
