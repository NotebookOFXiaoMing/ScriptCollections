import click
import pysam
import time

@click.command()
@click.option("--bam")
@click.option("--chrlist")
#@click.option("threads",default=1)
@click.option("--or1")
@click.option("--or2")

def get_mapped_paired_end_reads(bam,chrlist,or1,or2):

    fw01 = open(or1,'w')
    fw02 = open(or2,'w')
    chr_list = [line.strip() for line in open(chrlist,'r')]
    i = 0
    for chr_id in chr_list:
        read01 = {}
        read02 = {}
        for read in pysam.AlignmentFile(bam).fetch(chr_id):
            if read.is_mapped and read.is_read1 and read.mate_is_mapped:
                read01[read.to_dict()['name']] = [read.to_dict()['seq'],read.to_dict()['qual']]
            if read.is_mapped and read.is_read2 and read.mate_is_mapped:
                read02[read.to_dict()['name']] = [read.to_dict()['seq'],read.to_dict()['qual']]
                
        for read_id in read01.keys():
            if read_id in read02.keys():
                fw01.write("@%s\n%s\n+\n%s\n"%(read_id,read01[read_id][0],read01[read_id][1]))
                fw02.write("@%s\n%s\n+\n%s\n"%(read_id,read02[read_id][0],read02[read_id][1]))
        
        i += 1
        progress = len(chr_list)
        print('[{0}] INFO: {1}/{2} have been done!'.format(time.ctime(),i,progress))
    fw01.close()
    fw02.close()
    
if __name__ == '__main__':
    get_mapped_paired_end_reads()