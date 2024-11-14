def to_rna(dna_strand):
    nucleotide_complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_complement = ""
    for letter in dna_strand:
        rna_complement = rna_complement + nucleotide_complements[letter]

    return rna_complement