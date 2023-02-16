import click
from ete3 import NCBITaxa
import pandas as pd

@click.command()
@click.option("--species_list")
@click.option("--your_species")

def get_species_placement_in_NCBI(species_list,your_species):
    ncbi = NCBITaxa()
    df = pd.read_csv(species_list)
    for index,row in df.iterrows():
        if "Land Plants" in row['Organism Groups']:
            species_name = row['#Organism Name']
            name2taxid = ncbi.get_name_translator(names = [species_name])
            #print(name2taxid)
            if len(name2taxid) == 0:
                print(species_name)
            else:
                t_dict = ncbi.get_taxid_translator(ncbi.get_lineage(name2taxid[species_name][0]))
                #print(t_dict)
                if your_species in t_dict.values():
                    print(species_name,"_".join(t_dict.values()))
                    
                    
if __name__ == "__main__":
    get_species_placement_in_NCBI()