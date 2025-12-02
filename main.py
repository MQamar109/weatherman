# This is a sample Python script.
import parser
from handlers import get_year_calculations_and_date, calculate_month_averages, draw_combine_horizontal_bar_graph, \
    draw_horizontal_bar_graph

if __name__ == '__main__':
    args = parser.get_parser()

    if args.year:
        get_year_calculations_and_date(args.path, args.year)

    if args.month:
        calculate_month_averages(args.path, args.month)

    if args.graph:
        draw_horizontal_bar_graph(args.path, args.graph)

    if args.combine_graph:
        draw_combine_horizontal_bar_graph(args.path, args.combine_graph)
