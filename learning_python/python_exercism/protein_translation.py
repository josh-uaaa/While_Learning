CODONS_DICT = {'Methionine': ('AUG'),
               'Phenylalanine': ('UUU', 'UUC'),
               'Leucine': ('UUA', 'UUG'),
               'Serine': ('UCU', 'UCC', 'UCA', 'UCG'),
               'Tyrosine': ('UAU', 'UAC'),
               'Cysteine': ('UGU', 'UGC'),
               'Tryptophan': ('UGG'),
               'STOP': ('UAA', 'UAG', 'UGA')}

def proteins(strand):
    codons_in_strand = []
    for i in range(0, len(strand), 3):
        codons_in_strand.append(strand[i:i + 3])
    protein_translation = []
    for codon in codons_in_strand:
        if codon not in CODONS_DICT.get('STOP'):
            for protein, codons_list in CODONS_DICT.items():
                if codon in codons_list:
                    protein_translation.append(protein)
        else:
            break

    return protein_translation