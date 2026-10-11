import collections


Neucleotides = ['A', 'C', 'G', 'T']

def ValidateSequence(dna_sequence):   #input needs to be a string

    tmp = dna_sequence.upper()
    for i in tmp:
        if i not in Neucleotides:
            return False
    return tmp

def CountNucFrequency(sequence):
    # tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    # for i in sequence:
    #     tmpFreqDict[i] += 1
    # return tmpFreqDict
    return dict(collections.Counter(sequence))
    
 