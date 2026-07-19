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
            elif line_count == 2:
                read["seperator"] = "+"
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
        if not read["phred_score"]:
            continue

        if len(read["phred_score"]) != len(read["sequence"]):
            continue

        total_phred = sum(ord(c) - 33 for c in read["phred_score"])
        avg_phred = total_phred / len(read["phred_score"])

        if avg_phred >= quality:
            filtered_reads.append(read)

    
    return filtered_reads