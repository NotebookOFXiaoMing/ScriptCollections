import sys
import re
import numpy as np
from Bio import SeqIO


input_fa = sys.argv[1]

seq_len = []

for rec in SeqIO.parse(input_fa,'fasta'):
    seqs = re.split("N{10,}",str(rec.seq))
    for seq in seqs:
        seq_len.append(len(seq))
    
seq_len.sort(reverse=True)

seq_len_cumsum = list(np.cumsum(seq_len))

total_length = np.sum(seq_len)

Nx = {"N10":[],
      "N20":[],
      "N30":[],
      "N40":[],
      "N50":[],
      "N60":[],
      "N70":[],
      "N80":[],
      "N90":[],
      "N100":[]}

for i,j in enumerate(seq_len_cumsum):
    if j >= 0.1*total_length and j < 0.2*total_length:
        #print("N10: ",)
        Nx["N10"].append(seq_len[i])
    elif j >= 0.2*total_length and j < 0.3*total_length:
        #print("N20: ",seq_len[i])
        Nx["N20"].append(seq_len[i])
    elif j >= 0.3*total_length and j < 0.4*total_length:
        #print("N30: ",seq_len[i])
        Nx["N30"].append(seq_len[i])
    elif j >= 0.4*total_length and j < 0.5*total_length:
        #print("N40: ",seq_len[i])
        Nx["N40"].append(seq_len[i])
    elif j >= 0.5*total_length and j < 0.6*total_length:
        #print("N50: ",seq_len[i])
        Nx["N50"].append(seq_len[i])
    elif j >= 0.6*total_length and j < 0.7*total_length:
        #print("N60: ",seq_len[i])
        Nx["N60"].append(seq_len[i])
    elif j >= 0.7*total_length and j < 0.8*total_length:
        #print("N70: ",seq_len[i])
        Nx["N70"].append(seq_len[i])
    elif j >= 0.8*total_length and j < 0.9*total_length:
        #print("N80: ",seq_len[i])
        Nx["N80"].append(seq_len[i])
    elif j >= 0.9*total_length and j < 1*total_length:
        #print("N90: ",seq_len[i])
        Nx["N90"].append(seq_len[i])
    elif j >= 1*total_length:
        #print("N100: ",seq_len[i])
        Nx["N100"].append(seq_len[i])
        
for key,value in Nx.items():
    print(key,value[0])