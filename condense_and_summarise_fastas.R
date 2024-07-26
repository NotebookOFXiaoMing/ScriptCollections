#### redirect output and messages/errors to the log ####


args <- commandArgs(trailingOnly = TRUE)

#### get all the snakemake variables ####
maf2fasta_output <- args[1]

final_fasta <- args[2]
pair_summary_file <- args[3]
mask_fasta <- args[4]

# we need the target sequence name for a few things.
# because lastz munges names with dots in them, we just use the output
# file name, which has the {tchrom} on it.
tchrom = args[5]


#### Do the rest ####

library(tidyverse)


# read the sequences in.  They are on every other line.  The first
# is the target, the following are separate ones for each query chromosome
seqs <- read_lines(maf2fasta_output)

# break those sequences into a list of vectors
seq_vec_list <- str_split(seqs[seq(2, length(seqs), by = 2)], pattern = "")

snames <- seqs[seq(1, length(seqs), by = 2)]
rm(seqs)

# if there were multiple query sequences, condense them into a single one.
# the "-" has the lowest value of any of the possible letters in the aligned
# sequences, so this step takes the base at the aligned query sequence, if there
# is an aligned query sequency. (Remember we did single_cov2 so there will be only
# one aligned query at any point.)
if(length(seq_vec_list) > 2) {
  anc <- do.call(pmax, seq_vec_list[-1])
} else {
  anc <- seq_vec_list[[2]]
}

# now, we count up the number of different types of sites
pair_counts <- table(paste(seq_vec_list[[1]], anc))

# and make a tibble of those numbers
count_summary <- tibble(
  name = names(pair_counts),
  n = as.integer(pair_counts)
) %>%
  separate(name, into = c("target", "ancestral"), sep = " ") %>%
  mutate(chrom = tchrom, .before = target)

# and write that file out
write_csv(count_summary, file = pair_summary_file)


# and now, from anc, we subset out the sites that are "-"s in the target.
# That gives us an ancestral sequence that is congruent with the
# original target sequence. And then we replace the "-"'s in the ancestral
# seq with Ns
anc_fasta_seq <- anc[seq_vec_list[[1]] != "-"]
anc_fasta_seq[anc_fasta_seq == "-"] <- "N"


# We also create a fasta that masks the sites that are considered
# to be in repeat regions in either the target or the ancestral
# genome.  This is done by marking any position that is not a
# capital letter A, C, G, or T
# in both sequences an N, and anything that is a capital lettter
# A, C, G, or T in both a P.
# Note that this also chucks sites that are designated by IUPAC codes
# in the query.  Hmmm....
targ_seq <- seq_vec_list[[1]]
targ_seq <- targ_seq[targ_seq != "-"]

mask_seq = ifelse(
  (targ_seq %in% c("A", "C", "G", "T")) & (anc_fasta_seq %in% c("A", "C", "G", "T")),
  "P",
  "N"
  )




# now make a matrix out of those (anc_fasta_seq and mask_seq) to print them in lines.
# We have to extend each with NAs to be a length that is a multiple of 70 so that
# it doesn't get chopped off when we make a matrix of it for fast printing.


final_line_bits <- length(anc_fasta_seq) %% 70
if(final_line_bits != 0) {
  length(anc_fasta_seq) <- length(anc_fasta_seq) + (70 - final_line_bits)
  length(mask_seq) <- length(mask_seq) + (70 - final_line_bits)
}

# now, make a matrix of those and write them out.  We ensure that
# the NA's in the last row of the matrix are just empty (i.e. ""'s).


# writing out the ancestral fasta
cat(">", tchrom, "\n", sep = "", file = final_fasta)
matrix(anc_fasta_seq, ncol = 70, byrow = TRUE) %>%
  write.table(
    file = final_fasta,
    sep = "",
    na = "",
    quote = FALSE,
    append = TRUE,
    row.names = FALSE,
    col.names = FALSE
  )



# writing out the mask fasta
cat(">", tchrom, "\n", sep = "", file = mask_fasta)
matrix(mask_seq, ncol = 70, byrow = TRUE) %>%
  write.table(
    file = mask_fasta,
    sep = "",
    na = "",
    quote = FALSE,
    append = TRUE,
    row.names = FALSE,
    col.names = FALSE
  )