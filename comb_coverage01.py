import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(description="Combine remapping file")
    parser.add_argument("-g", "--graph", help="Graph type")
    parser.add_argument("-a", "--assembly", help="Graph type")
    parser.add_argument("-o", "--output", help="Graph type")
    parser.add_argument("-r", "--refornot", help="Graph type")
    return parser.parse_args()


def parse_node_coverage(line):
    # S       s34     CGTGACT LN:i:7  SN:Z:1  SO:i:122101     SR:i:0  dc:f:0
    # "nodeid","nodelen","chromo","pos","rrank",assemb
    """
    Parse the gaf alignment
    Input: line from gaf alignment
    Output: tuple of nodeid, nodelen, start_chromo, start_pos, coverage

    """
    line_comp = line.strip().split()
    nodeid = line_comp[1]
    nodelen = len(line_comp[2])
    start_chromo = line_comp[4].split(":")[2]
    start_pos = line_comp[5].split(":")[2]
    rrank = line_comp[-2].split(":")[2]
    coverage = line_comp[-1].split(":")[2]

    return nodeid, nodelen, start_chromo, start_pos, rrank, coverage


if __name__ == "__main__":
    args = parse_args()
    graph = args.graph
    assembly = args.assembly
    output_tsv = args.output
    refOrNot = args.refornot
    
    if refOrNot == "Y":
        fr = open(graph,'r')
        combcov = pd.DataFrame([parse_node_coverage(line) for line in fr if line.startswith("S")],
                                columns=["nodeid", "nodelen", "start_chromo", "start_pos", "rrank", assembly])
    
        combcov.to_csv(output_tsv,sep="\t",index=False)
    elif refOrNot == "N":
        fr = open(graph,'r')
        combcov = pd.DataFrame([[parse_node_coverage(line)[0], parse_node_coverage(line)[-1]] for line in fr if line.startswith("S")],
                                  columns=["nodeid", assembly])
        combcov.to_csv(output_tsv,sep="\t",index=False)