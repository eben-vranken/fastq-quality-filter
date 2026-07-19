from argparse import ArgumentParser

from src import parser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("path", help="Path to the FastQ file to be parsed.")
    parser.add_argument("-q", "--quality", required=True, help="Minimum quality to be shown")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    parser.parse_fastq(args.path)