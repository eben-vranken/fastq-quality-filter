def parse_fastq(file_path):
    with open(file_path) as fp:
        for line in fp:
            print(line.strip())