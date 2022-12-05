# 01_BIO_DeNovoAssembly

## Project Description

Data is in fasta format. Every two lines represents a read (a DNA fragment) with 60bp. The first line started with ‘>’ contains the name of the read and the second line is the nucleotide sequence. 

Tips: 
- Repeated sequences larger than 25bp do not occur in original sequence. 
- Each read overlaps at least 25bp with other reads.

## Project objectives
These reads (DNA fragments) of repeated sequences overlap. The task is to construct a de novo method to assemble these reads and obtain the gene sequence. 

### Code file: https://github.com/ybezginova2016/01_BIO_DeNovoAssembly/blob/main/main_DeNovoAssembly.ipynb

### Relevant Readings:

- Palmer, L. E., Dejori, M., Bolanos, R., & Fasulo, D. (2010). Improving de novo sequence assembly using machine learning and comparative genomics for overlap correction. BMC bioinformatics, 11(1), 1-9.

- Padovani de Souza, K., Setubal, J. C., Ponce de Leon F. de Carvalho, A. C., Oliveira, G., Chateau, A., & Alves, R. (2019). Machine learning meets genome assembly. Briefings in Bioinformatics, 20(6), 2116-2129.

- https://towardsdatascience.com/genome-assembly-using-de-bruijn-graphs-69570efcc270
- https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259
