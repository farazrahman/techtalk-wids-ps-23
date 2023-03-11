import os
import pandas as pd
from Bio import Entrez
import ssl
import subprocess
# ssl._create_default_https_context = ssl._create_unverified_context


# set the SRA ID to download
sra_accession = "SRR17066006"

# Use subprocess to run the prefetch command in the shell
subprocess.run(['/Users/farazrahman/techtalk-wids-ps-23/sratoolkit.3.0.1-mac64/bin/prefetch', 'SRR17066006'])

# Use subprocess to run the fasterq-dump command to convert the SRA data to fastq format
subprocess.run(['/Users/farazrahman/techtalk-wids-ps-23/sratoolkit.3.0.1-mac64/bin/fastq-dump', 'SRR17066006'])