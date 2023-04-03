from Bio import SeqIO
import pandas as pd


def parse_fastq(input_file: str)-> pd.DataFrame:
    """
    Parses a fastq file and returns a pandas DataFrame with the sequence, quality scores, and ID of each record.
    :param input_file:
    :return:
    """

    # Read in the fastq file using SeqIO.parse()
    records = SeqIO.parse(input_file, "fastq")

    # Initialize lists to store the sequences, quality scores, and IDs
    seqs = []
    quals = []
    ids = []

    # Loop through each record in the fastq file and extract its sequence, quality scores, and ID
    for record in records:
        seqs.append(str(record.seq))
        quals.append(record.letter_annotations["phred_quality"])
        ids.append(record.id)

    # Create a dictionary containing the ID, sequence, and quality score information
    data = {
        "id": ids,
        "sequence": seqs,
        "quality_scores": quals
    }

    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data)

    print(df['sequence'])

    return df


if __name__ == '__main__':
    fastq_file = "SRR17066006.fastq"
    fastq_df = parse_fastq(fastq_file)
