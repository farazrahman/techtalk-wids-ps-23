import pandas as pd
import os


def parse_fastq(input_file: str) -> pd.DataFrame:
    """
    Parses a FastQ file and returns a pandas dataframe containing sequence ID,
    seq_reads, and sequence quality.
    :param input_file: Path to the FastQ file
    :return: Dataframe
    """
    sequence_list = []
    read_lines = []

    # open and read all lines in the fastq file
    with open(input_file, 'r') as fastq_file:
        for lines in fastq_file:
            read_lines.append(lines.rstrip('\n'))

    # break into groups of 4
    for line in range(0, len(read_lines), 4):
        single_sequence = read_lines[line:line + 4]
        if single_sequence[0].startswith('@') and (len(single_sequence[1]) == len(single_sequence[3])):
            sequence_list.append(single_sequence)
        else:
            print(f'sequence mismatch with id starts with {single_sequence[0][0]}, '
                  f'read length {len(single_sequence[1])}, quality length {len(single_sequence[3])}')

    print(f"The count of reads is {len(sequence_list)}")

    sequence_df = pd.DataFrame(sequence_list, columns=['seq_id', 'seq_reads', 'id2', 'seq_quality'])
    print(f"printing the first few rows of {sequence_df.head()}")

    return sequence_df


if __name__ == '__main__':
    df = parse_fastq('SRR17066006.fastq')
    print(df['seq_quality'])