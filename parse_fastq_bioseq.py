from Bio import SeqIO
import pandas as pd


def parse_fastq(input_file: str):
    records = SeqIO.parse(input_file, "fastq")

    seqs = []
    quals = []
    ids = []

    for record in records:
        seqs.append(str(record.seq))
        quals.append(record.letter_annotations["phred_quality"])
        ids.append(record.id)

    data = {
        "id": ids,
        "sequence": seqs,
        "quality_scores": quals
    }

    df = pd.DataFrame(data)

    print(df['sequence'])

    return df


if __name__ == '__main__':
    fastq_file = "SRR17066006.fastq"
    fastq_df = parse_fastq(fastq_file)
