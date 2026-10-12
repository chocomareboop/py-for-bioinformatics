import collections
from os import replace
from Sequences import *


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
    
def Transcription(seq):          #replacing T with U in the DNA sequence to get RNA sequence
   return seq.replace("T", "U")

def ReverseComplement(seq):      
    '''returning the reverse complement of the DNA sequence'''
    return ''.join([ReverseNeucleotides[i] for i in seq])[::-1]
