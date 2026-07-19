def output_filtered(filtered_reads, file):
    f = open(file, "w")

    for reads in filtered_reads:
        for _, v in reads.items():
            f.write(v)
            f.write("\n")