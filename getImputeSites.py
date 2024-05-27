# 1 impute vcf gz
# 2 truth.sites
# 3 output

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1],comment="#",sep="\t",header=None)

fw = open(sys.argv[3],'w')

with open(sys.argv[2],'r') as fr:
    for line in fr:
        row = int(line.strip().split()[0])
        col = int(line.strip().split()[1])
        trueGT =  line.strip().split()[2]
        imputeGT = df.iloc[row-1,col-1]
        
        fw.write("%d\t%d\t%s\t%s\n"%(row,col,trueGT,imputeGT))
        
fw.close()