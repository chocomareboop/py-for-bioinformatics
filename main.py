from DNAToolkit import *
import random
from utilities import *

DNAstr = "ATTCTghAGC"
randDNAstr =  ValidateSequence(
              ''.join(
                  [random.choice(Neucleotides)
                      for i in range(20)]))

print(colored(randDNAstr))
print(CountNucFrequency(randDNAstr))
print(Transcription(randDNAstr))
print(ReverseComplement(randDNAstr))


