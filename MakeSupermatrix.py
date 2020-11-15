"""
A script for making supermatrix
@author: Luming Lin
"""


from Bio import SeqIO
from Bio import AlignIO
from Bio.Alphabet import IUPAC, Gapped
from Bio.Nexus import Nexus
import sys

# feed file names to script
MSAfileList = sys.argv[1] # the file stores MSA

# get names of one-gene MSA files
with open(str(MSAfileList),"r") as f:
  MSAfilenames = []
  file_list = []
  for line in f:
    MSAfilename = line.replace("\n",'') 
    MSAfilenames.append(MSAfilename) # get names of MSA files without format

# transform fasta to nex format
for MSAfilename in MSAfilenames:
  file_list.append("speciesID_" + MSAfilename + ".nex") # get names of MSA files in "nex" format
  with open(MSAfilename + ".fa", "rU") as input_handle, open("speciesID_" + MSAfilename + ".nex", "w") as output_handle_nex, open("speciesID_" + MSAfilename + ".fa", "w") as output_handle_fasta:
      alignments = AlignIO.read(input_handle, "fasta", alphabet=Gapped(IUPAC.protein)) # read fasta file to "alignments"
      for seq in alignments:
        seq.id = seq.description.split("[")[-1][:-1] # use species name as sequence ID
        seq.description = "" # use species name as sequence ID
      AlignIO.write(alignments, output_handle_nex, "nexus") # write "alignments" with new ID to nexus format
      AlignIO.write(alignments, output_handle_fasta, "fasta") # to fasta format

# change a one-gene MSA nex file to a nex obeject, and put them together    
nexi =  [(fname, Nexus.Nexus(fname)) for fname in file_list] 

# combine one-gene MSA nex file of different genes
combined = Nexus.combine(nexi)
# write combined MSA to a nex file 
combined.write_nexus_data(filename=open('supermatrix.nex', 'w')) 

# transform nex to fasta format
with open("supermatrix.nex", "rU") as input_handle, open("supermatrix.fa", "w") as output_handle:
  alignments = AlignIO.read(input_handle, "nexus", alphabet=Gapped(IUPAC.protein))
  AlignIO.write(alignments, output_handle, "fasta")



