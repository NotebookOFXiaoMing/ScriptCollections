library(GenomicFeatures)
library(tidyverse)

args <- commandArgs(trailingOnly = TRUE)

anno <- makeTxDbFromGFF(args[1], format = "auto")

tx_lens <- transcriptLengths(anno, with.cds_len = TRUE)

tx_lens %>% 
  filter(cds_len>0) %>% 
  group_by(gene_id) %>% 
  top_n(n=1,wt=tx_len) %>% 
  distinct(gene_id,.keep_all = TRUE) %>% 
  pull(tx_name) %>% 
  write_lines(args[2])