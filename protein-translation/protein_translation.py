protein_tuples = [
    (['AUG'], 'Methionine'),
    (['UUU', 'UUC'], 'Phenylalanine'),
    (['UUA', 'UUG'], 'Leucine'),
    (['UCU', 'UCC', 'UCA', 'UCG'], 'Serine'),
    (['UAU', 'UAC'], 'Tyrosine'),
    (['UGU', 'UGC'], 'Cysteine'),
    (['UGG'], 'Tryptophan'),
    (['UAA', 'UAG', 'UGA'], 'STOP')
]

def proteins(strand):
    if len(strand) % 3 != 0: raise Exception("A DNA strand's length must be a multiple of 3")
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []
    for codon in codons:
        for t in protein_tuples:
            if codon in t[0]:
                if t[1] == 'STOP':
                    return result
                elif t[1] not in result:
                    result.append(t[1])
    
    return result


print(protein_tuples[0][1])