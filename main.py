import argparse

from csv_parser import load_exempt, load_data
from data_aggregator import aggregate
from plot import generate_plots


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, help='filepath to csv file with the lifting data', default='data.csv')
    parser.add_argument('--exempt', type=str, help='filepath to csv file with rows to exclude', default='exempt.csv')
    args = parser.parse_args()

    exempt = load_exempt(args.exempt)
    data = load_data(args.data, exempt)
    print(f'Loaded {args.data} and {args.exempt}')

    aggregation = aggregate(data)
    plots = generate_plots(aggregation)


if __name__ == '__main__':
    main()