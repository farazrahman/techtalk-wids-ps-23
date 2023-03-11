# techtalk-wids-ps-23

## ncbi_data_fetch
How to fetch and parse SRA data from NCBI for further use in analytics.

#### This repository locates the First SARS-CoV-2- Omicron variant data in the NCBI's website, downloads the Sequence Read Archive (SRA) data using the following two methods:
  - NCBI's SRA toolkit and CLI commands to dowload the SRA data in fastq format and then uses a python script to parse the fastq file.
  - NCBI's SRA toolkit and using the shell commands using the python subprocess library and then uses a python script to parse the fastq file with and without using an external library.


#### Workflow:

![Workflow](https://github.com/farazrahman/ncbi_data_fetch/blob/main/NCBI%20Data%20Engineering%20Workflow.jpg)

#### 1. LOCATE THE DATA:
- Locate the data in NCBI website: First SARS-CoV-2- Omicron variant in Europe and note the SRR run id i.e. SRR17066006
Link: https://www.ncbi.nlm.nih.gov/sra/?term=omicron+europe


#### 2. DOWNLOAD AND INSTALL THE SRA TOOLKIT:
- In order to access the fastq file through the NCBI CLI commands, we need to download and install the SRA toolkit provided by NCBI to access and manipulate custom data from NCBI’s website. https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit#ncbi-sra-toolkit


- Download and install the SRA toolkit using the curl command in the project directory:
  ```
  Curl –output sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-mac64.tar.gz
  ```

- Extract the content using the command below: 
    ```
    tar -vxzf sratoolkit.tar.gz
    ```

- Append the path to the binaries to your PATH environment variable (Important: Make sure the version of SRA toolkit is same as the one that you have downloaded).and verify the binaries:
    ````
    export PATH=$PATH:$PWD/sratoolkit.3.0.1-mac64/bin
  ````

- Verify the binaries and check if everything is in place by checking `which fastq-dump` or `which prefetch`. This should give the path something like `/Users/farazrahman/techtalk-wids-ps-23/sratoolkit.3.0.1-mac64/bin/fastq-dump`:
    ````
    which fastq-dump
    ````
- Configure the toolkit to access the data on the cloud and follow the instructions provided here `https://github.com/ncbi/sra-tools/wiki/03.-Quick-Toolkit-Configuration` to finish :
    ````
    vdb-config -i
    ````

### 3. There are two options shown in this repository to download the SRA data. One using the CLI (provided in point 3.2 below) and other option (provided in point 3.1 below) is to use python to download the data. 

#### 3.1 DOWNLOAD THE SRA DATA USING PYTHON SUBPROCESS:
- Follow the code and instructions in `fetch_fastq.py`

#### 3.2 DOWNLOAD THE SRA DATA USING THE CLI:
- Once the SRA toolkit is configured, use the prefetch tool from the SRA toolkit to download the SRA data  using the following command: 
    ````
    Vdb-config -prefetch-to-cwd
    ````
    ````
    Prefetch SRR17066006
    ````

- Use the fastq-dump tool to convert the SRA data to fastq format:
    ````
    Fasterq-dump SRR17066006
    ````

#### 4. PARSE AND ANALYZE THE SRA DATA WHICH IS IN FASTQ FORMAT:

- Refer `parse_fastq_bioseq.py` to parse fastq file using the `Biopython` library
- Refer `parse_fastq.py` to use python to parse fastq file for analysis. 
- Refer `analyze-fastq.ipynb` to run some basic visualizations like checking the quality, base count (ATCG) and distribution of read length.


#### 5. RUN FASTQC FOR QUALITY CHECK:

- Download the FastQC(a quality control tool for high thorughput sequence data) from https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
and run the quality check



NOTE:
- The NCBI websites provides many more ways to download and analyze the datasets. To explore more visit: `https://www.ncbi.nlm.nih.gov/home/tools/`
