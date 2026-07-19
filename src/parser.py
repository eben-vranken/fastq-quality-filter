def parse_fastq(file_path):
    reads = []
    read = {}

    line_count = 0
    with open(file_path) as fp:
        for line in fp:
            line = line.strip()
            if line_count == 0:
                read["title"] = line
            elif line_count == 1:
                read["sequence"] = line
            elif line_count == 3:
                read["phred_score"] = line

            line_count += 1
            
            if line_count == 4:
                line_count = 0
                reads.append(read)
                read = {}

    for read in reads:
        print(read)