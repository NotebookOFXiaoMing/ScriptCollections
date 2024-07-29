import sys


## list1 指定顺序的列表
## list2 需要调整顺序的列表
def find_positions(list1,list2):
    positions = []
    for element in list1:
        position = list2.index(element)
        positions.append(position + 9)
        
    return(list(range(9)) + positions)

## sys.argv[1] 样本顺序文件,每行一个样本
## sys.argv[2] 输入vcf
## sys.argv[3] 输出vcf

sample_order_list = []

with open(sys.argv[1],'r') as fr:
    for line in fr:
        sample_order_list.append(line.strip())

fr = open(sys.argv[2],'r')
fw = open(sys.argv[3],'w')

for line in fr:
    if line.startswith("##"):
        fw.write(line)

    elif line.startswith("#CHROM"):
        raw_sample_order = line.strip().split()[9:]

        order_list = find_positions(sample_order_list,raw_sample_order)

        temp_list = line.strip().split()

        new_list = [temp_list[i] for i in order_list]

        fw.write("%s\n"%('\t'.join(new_list)))

    else:
        temp_list = line.strip().split()

        new_list = [temp_list[i] for i in order_list]

        fw.write("%s\n"%('\t'.join(new_list)))

fr.close()
fw.close()

