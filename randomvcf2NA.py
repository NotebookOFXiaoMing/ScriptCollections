# 1 input vcf
# 2 output vcf
# 3 truth sites

import sys
import random

fr = open(sys.argv[1],'r')
fw = open(sys.argv[2],'w')
fw02 = open(sys.argv[3],'w')

row = 0
col = 0

for line in fr:
    if line.startswith("#"):
        fw.write(line)
    else:
        row += 1
        temp_list = line.strip().split("\t")
        
        if random.random() <= 0.1:
            new_list = []
            for i in range(0,len(temp_list)):
                if i < 9:
                    new_list.append(temp_list[i])
                elif i >= 9:
                    if random.random() <= 0.2:
                        new_list.append("./.")
                        GT = temp_list[i][0:3]
                        
                        fw02.write("%d\t%d\t%s\n"%(row,i+1,GT))
                    else:
                        new_list.append(temp_list[i])
            
            fw.write('%s\n'%("\t".join(new_list)))
            
            
            
        else:
            fw.write('%s\n'%("\t".join(temp_list)))
            
fw.close()
fw02.close()
fr.close()