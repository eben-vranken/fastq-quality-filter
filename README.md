<h1 align="center">🧬 FastQ Quality Filter</h1>

<p align="center">
    A command-line utility to filter low-quality reads out of a FASTQ file.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI built to perform basic sequencing quality control. It parses a FASTQ file, scores each read by its average Phred quality, discards reads that fall below a given threshold, and writes the surviving reads to a new FASTQ file.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/fastq-quality-filter.git
cd fastq-quality-filter
```

## Usage

Pass the path to a FASTQ file, a minimum quality with `-q`, and an output path with `-o`. All three are required.

```bash
python fastq-quality-filter.py data/simulated-fastq.fastq -q 20 -o filtered.fastq
```

### Short Flags

The same arguments are available in short form:

```bash
python fastq-quality-filter.py data/simulated-fastq.fastq -q 20 -o filtered.fastq
```

### Example Output

Given a FASTQ file with reads scoring above and below the threshold, only the reads that pass get written to the output file:

```
@READ_01_CLASSIC_DROP_OFF
ATGCGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTAC
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIBA@@???>=<;:9876543210///
@READ_02_ADAPTER_CONTAMINATION
GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAAAGCTTGGCGTAATCATGGTCATAGCTG
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII,,,,+++++++++!!!!!!!!!%%%%%%
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `path` | *File path* | *None* | Path to the FASTQ file to be parsed. Required, positional. |
| `-q`, `--quality` | *Integer* | *None* | Minimum average Phred quality a read must meet to be kept. Required. |
| `-o`, `--output` | *File path* | *None* | Path to write the filtered FASTQ file to. Required. |

## Feature Set

* **FASTQ Parsing:** Reads a file in 4-line blocks (title, sequence, separator, quality string) and builds a record for each read.
* **Average Quality Scoring:** Converts each read's quality string to Phred scores using ASCII-33 encoding, then averages them across the read.
* **Whole-Read Filtering:** Discards a read entirely if its average score falls below the threshold, rather than trimming individual low-quality bases.
* **Malformed Record Handling:** Skips any read where the sequence and quality strings differ in length, instead of scoring it incorrectly.
* **FASTQ Output:** Writes the surviving reads back out in valid FASTQ format.

## Limitations

This parser only supports standard 4-line-per-read FASTQ files (title, sequence, separator, quality string). It does not handle multi-line FASTQ variants, where a single read's sequence or quality string is wrapped across more than one line.

## License

MIT