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

    return reads

def filter_reads(reads, quality):
    filtered_reads = []
    for read in reads:
        filtered_read = {}
        filtered_read["title"] = read["title"]
        filtered_read["sequence"] = ""
        filtered_read["phred_score"] = ""
        print(len(read["sequence"]))
        print(len(read["phred_score"]))
        for i in range(0, len(read["sequence"])):
            phred = ord(read["phred_score"][i]) - 33
            if phred >= quality:
                filtered_read["sequence"] += read["sequence"][i]
                filtered_read["phred_score"] += read["phred_score"][i]

        filtered_reads.append(filtered_read)

    for read in filtered_reads:
        print(read)
        print()