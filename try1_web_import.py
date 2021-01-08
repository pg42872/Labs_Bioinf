from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq

#Tentar importar o gene PHB do NCBI

Entrez.email = "jpsfreitas12@gmial.com"
handle = Entrez.efetch(db = "nucleotide",rettype="genbank", retmode="text", id = "NC_000017.11")
seq_record = SeqIO.read(handle,"genbank")
handle.close()

seq_record
seq_record.annotations


Entrez.email = "jpsfreitas12@gmial.com"  # Always tell NCBI who you are
handle = Entrez.efetch(db="nucleotide", id="NC_000017.11", rettype="gb", retmode="text")
print(handle.read())
