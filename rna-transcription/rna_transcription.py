nucleotide_complement_map = {
    'G' : 'C',
    'C' : 'G',
    'T' : 'A',
    'A' : 'U'
}

def to_rna(dna_strand):
    return ''.join([nucleotide_complement_map.get(nucleotide) for nucleotide in dna_strand])
