import sys
import random

# 1 input vcf
# 2 output vcf
# 3 proportion 0-100
# 3 seed number

random.seed(sys.argv[4])

with open(sys.argv[2],'w') as fw:
    with open(sys.argv[1],'r') as fr:
        for line in fr:
            if line.startswith("#"):
                fw.write(line)
            else:
                random_number = random.random()
                if random_number < float(sys.argv[3])/100:
                    fw.write(line)
                    
                    
print("Good Job!")