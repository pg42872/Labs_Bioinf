from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Blast import NCBIWWW, NCBIXML

#Proibitina-2

pro2 = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/Proibitina-2/sequence.fasta"),"fasta")
pro2

#BLAST de proteinas 
blast = NCBIWWW.qblast("blastp", "nr", pro2.format("fasta"))

save_file = open("my_blast_pro2.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()
