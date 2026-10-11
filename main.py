from DNAToolkit import *
import random

DNAstr = "ATTCTghAGC"
randDNAstr =  ValidateSequence(
              ''.join(
                  [random.choice(Neucleotides)
                      for i in range(20)]))

print(randDNAstr)
print(CountNucFrequency(randDNAstr))


