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

#LOCALIZAÇÃO SUB CELULAR

#Usando a ferramenta on-line Cell-Ploc 2.0
#Citation
#Hong-Bin Shen, and Kuo-Chen Chou, "Virus-mPLoc: a fusion classifier for viral protein subcellular location prediction by incorporating multiple sites", Journal of Biomolecular Structure & Dynamics, 2010, 28: 175-86.
#Kuo-Chen Chou and Hong-Bin Shen: "Cell-PLoc: A package of web-servers for predicting subcellular localization of proteins in various organisms", Nature Protocols, 2008, 3: 153-162.
#Hong-Bin Shen and Kuo-Chen Chou, "Virus-PLoc: A fusion classifier for predicting the subcellular localization of viral proteins within host and virus-infected cells.", Biopolymers. 2007, 85, 233-240.
#Kuo-Chen Chou, "Using amphiphilic pseudo amino acid composition to predict enzyme subfamily classes". Bioinformatics, 2005, 21, 10-19.
#-Bin Shen and Kuo-Chen Chou, "Ensemble classifier for protein folding pattern recognition". Bioinformatics, 2006, 22, 1717-1722.

#Quando o virus infeta o hospediro, esta proteina encontra-se no citoplasma do hospedeiro


#??????????
#Usando a ferramenta on-line LocTree3
#Citation
#Goldberg T, Hecht M, Hamp T, Karl T, Yachdav G, Nielsen H, Rost B et al. LocTree3 prediction of localization. Nucleic Acids Research 2014. PMID: 24848019; Goldberg T, Hamp T and Rost B: LocTree2 predicts localization for all domains of life. Bioinformatics 2012, 28:i458-i465. PMID: 22962467

#Com um score de 100 e precisao de 99% diz que esta proteína é secretada para fora do organismo


#Usando o PSORT para organismos de reino Archea
#Diz que a proteina se encontra no citoplasma


#DOMINIOS TRANSMEMBRANARES

#Usando o Phobius, diz que tem 1 unico dominio não citoplasmático

#Usando o TMHMM, diz que está do lado extracelular