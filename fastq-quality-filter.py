from argparse import ArgumentParser

from src import parser
from src import outputter

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("path", help="Path to the FastQ file to be parsed.")
    
    parser.add_argument("-q", "--quality", required=True, help="Minimum quality to be shown")
    parser.add_argument("-o", "--output", required=True, help="Path to new filtered file output")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    reads = parser.parse_fastq(args.path)

    filtered_reads = parser.filter_reads(reads, int(args.quality))

    outputter.output_filtered(filtered_reads, args.output)