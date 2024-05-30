import sys

fw = open(sys.argv[2],'w')

with open(sys.argv[1],'r') as fr:
    for line in fr:
        if line.startswith("#"):
            fw.write(line)
        else:
            temp_list = line.strip().split("\t")
            
            if len(temp_list[3]) == len(temp_list[4]):
                temp_list[2] = temp_list[0] + "_" + temp_list[1] + "_SNP"
            else:
                temp_list[2] = temp_list[0] + "_" + temp_list[1] + "_INDEL"
                temp_list[3] = "A"
                temp_list[4] = "T"
            
            fw.write("%s\n"%('\t'.join(temp_list)))
            
fw.close()