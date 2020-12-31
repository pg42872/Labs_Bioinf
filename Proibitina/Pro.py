from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Blast import NCBIWWW, NCBIXML

#NSP2

pro = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/Proibitina/sequence.fasta"),"fasta")
pro

#BLAST de proteinas 
blast = NCBIWWW.qblast("blastp", "nr", pro.format("fasta"))

save_file = open("my_blast_pro.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()
