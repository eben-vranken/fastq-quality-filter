def output_filtered(filtered_reads):
    f = open("output.fastq", "w")

    for reads in filtered_reads:
        for _, v in reads.items():
            f.write(v)
            f.write("\n")