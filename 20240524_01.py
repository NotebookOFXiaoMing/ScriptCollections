import sys

fw = open(sys.argv[2],'w')

with open(sys.argv[1],'r') as fr:
    for line in fr:
        if line.startswith("#"):
            fw.write(line)
        else:
            temp_list = line.strip().split("\t")
            new_list = [None]*len(temp_list)
            
            new_list[0] = temp_list[0]
            new_list[1] = temp_list[1]
            new_list[2] = temp_list[0] + "_" + temp_list[1] + "_SV"
            new_list[3] = "A"
            new_list[4] = "T"
            new_list[5] = temp_list[5]
            new_list[6] = temp_list[6]
            new_list[7] = "."
            new_list[8] = "GT"
            
            new_list[9:] = ['./.' if j.count(".") > 0 else j for j in [i[0:3] for i in temp_list[9:]]]
            
            fw.write("%s\n"%('\t'.join(new_list)))
            
fw.close()