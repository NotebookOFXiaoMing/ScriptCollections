import sys
import re

fr = open(sys.argv[1],'r')
fw = open(sys.argv[2],'w')

def convertGTto012(x):
    if x == "0|0" or x == "0/0":
        return "0"
    elif x == "1|0" or x == "1/0" or x == "0|1" or x == "0/1":
        return "1"
    elif x == "1|1" or x == "1/1":
        return "2"
    
def extractGenotype(x):
    pattern = "[0-9][|/][0-9]"
    regexp = re.compile(pattern)
    
    return regexp.findall(x)[0]

for line in fr:
    if line.startswith("##"):
        continue
    elif line.startswith("#CHROM"):
        temp_list = line.strip().split("\t")
        new_list = ['snpid'] + temp_list[9:]
        fw.write("%s\n"%('\t'.join(new_list)))
            
    else:
        temp_list = line.strip().split("\t")
        
        id = temp_list[0] + "_" + temp_list[1] + "_" + sys.argv[3]
        
        new_list = [id] + [convertGTto012(extractGenotype(i)) for i in temp_list[9:]]
        
        fw.write("%s\n"%('\t'.join(new_list)))
        
        
fr.close()
fw.close()