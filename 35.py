seq = 'AGUUUAUAG'

print(seq.replace('U','T'))

from Bio.Seq import Seq

seq = Seq('AGTTTATAG')
print(seq.transcribe())
