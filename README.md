# Introduction
In evolutionary biology, "supermatrix" is a data matrix used to reconstruct genome phylogeny, which contains multiple sequence alignments (MSA) of multiple genes. 

A possible workflow for building supermatrix:

 1. Find ‘universal single-copy’ orthologues across the taxonomic group ([OrthoFinder](https://github.com/davidemms/OrthoFinder) and [Batch Web CD-Search Tool with Pfam database](https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi)).
 2. Make a multiple alignment of each orthogroup, respectively ([MAFFT](https://mafft.cbrc.jp/alignment/software/)).
 3. Concatenate the alignments. The length of one concatenated alignment is the sum of each orthogroup's MSA length.

(Barker, D 2020, _Lecture 4: Phylogeny_, lecture notes, Comparative and Evolutionary Genomics PGBI11115, The University of Edinburgh, delivered Feb 2020.)

# Requirements
 - Python 3
 - Bio
 - sys

# Input
 - several MSA(Multiple sequence alignments) files of orthogroups/genes, check `OG0000296ID_aligned.fa` and `OG0000298ID_aligned.fa` in `MSA/testFiles/Input` as an example.
- a file stores names of all MSA files, check `MSAfileNames.txt` in `MSA/testFiles/Input` as an example.

# Output
 - the supermatrix, like `supermatrix.fa` in `MSA/testFiles/Output`.

# Command
```
python3 MakeSupermatrix.py MSAfileNames.txt
```
