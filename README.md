# 01_BIO_DeNovoAssembly

## Project Description

Data is in fasta format. Every two lines represents a read with 60bp. The first line started with ‘>’ contains the name of the read and the second line is the nucleotide sequence. 

Tips: 
- Repeated sequences larger than 25bp do not occur in original sequence. 
- Each read overlaps at least 25bp with other reads.

## Project objectives
These reads of repeated sequences overlap. The task is to construct a de novo method to assemble these reads and obtain the gene sequence. 

### Relevantl Reading: https://thesequencingcenter.com/knowledge-base/de-novo-assembly/

### Code: https://github.com/ybezginova2016/01_BIO_DeNovoAssembly/blob/main/01_main_DeNovoAssembly.ipynb
