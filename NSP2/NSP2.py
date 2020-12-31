from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Blast import NCBIWWW, NCBIXML

#NSP2

nsp2 = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/NSP2/nsp2.fasta"),"fasta")
nsp2
###não é possivel download do ficheiro genbank

#BLAST de proteinas 
blast = NCBIWWW.qblast("blastp", "nr", nsp2.format("fasta"))

save_file = open("my_blast_nsp2.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()

#Leitura dos resultados do BLASTp
result = open("my_blast_nsp2.xml")
blast_records = NCBIXML.read(result)
blast_records