from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SwissProt
from urllib.request import urlopen


#Proibitina
#Ficheiro NCBI local
pro = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/sequence.fasta"),"fasta")
pro

#Abrir ficheiro SwissProt localmente FASTA
ficheiro = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/uniprot-yourlist_M20210105A94466D2655679D1FD8953E075198DA82BA1DF7.fasta"),"fasta")
ficheiro 

#Abrir ficheiro SwissProt localmente full infor
ficheiro = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/uniprot-yourlist_M20210102A94466D2655679D1FD8953E075198DA82A5A69C.txt")
ficheiro

record = SwissProt.read(ficheiro)
print(record.description)
print(record.references)

for ref in record.references:
    print("authors:", ref.authors)
    print("title:", ref.title)
    print(record.organism_classification)

#Abrir ficheiro SwissProt pela internet
url = "https://www.uniprot.org/uniprot/P35232.txt"
handle = urlopen(url)
handle 

recorde = SwissProt.read(handle)
recorde
print(recorde.description)
print(recorde.references)


#BLAST de proteinas 
blast = NCBIWWW.qblast("blastp", "nr", pro.format("fasta"))

save_file = open("my_blast_pro.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()

#Leitura dos resultados do BLASTp
result = open("my_blast_pro.xml")
blast_records = NCBIXML.read(result)
blast_records

E_VALUE_THRESH = 0.05
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print ('****Alignment****')
                    print ('sequence:', alignment.title)
                    print ('length:', alignment.length)
                    print ('e value:', hsp.expect)
                    
result.close()




#LOCALIZAÇÃO SUB CELULAR

#Usando a ferramenta on-line Cell-Ploc 2.0
#Citation
#Hong-Bin Shen, and Kuo-Chen Chou, "Virus-mPLoc: a fusion classifier for viral protein subcellular location prediction by incorporating multiple sites", Journal of Biomolecular Structure & Dynamics, 2010, 28: 175-86.
#Kuo-Chen Chou and Hong-Bin Shen: "Cell-PLoc: A package of web-servers for predicting subcellular localization of proteins in various organisms", Nature Protocols, 2008, 3: 153-162.
#Hong-Bin Shen and Kuo-Chen Chou, "Virus-PLoc: A fusion classifier for predicting the subcellular localization of viral proteins within host and virus-infected cells.", Biopolymers. 2007, 85, 233-240.
#Kuo-Chen Chou, "Using amphiphilic pseudo amino acid composition to predict enzyme subfamily classes". Bioinformatics, 2005, 21, 10-19.
#-Bin Shen and Kuo-Chen Chou, "Ensemble classifier for protein folding pattern recognition". Bioinformatics, 2006, 22, 1717-1722.

#Proteina situa-se na mitocondria e nucleo


#Usando a ferramenta on-line LocTree3
#Citation
#Goldberg T, Hecht M, Hamp T, Karl T, Yachdav G, Nielsen H, Rost B et al. LocTree3 prediction of localization. Nucleic Acids Research 2014. PMID: 24848019; Goldberg T, Hamp T and Rost B: LocTree2 predicts localization for all domains of life. Bioinformatics 2012, 28:i458-i465. PMID: 22962467

#Proteina situa-se na membrana mitocondrial


#Usando o PSORT para organismos de reino Euckarya
#Diz que a proteina se encontra no citoplasma


#DOMINIOS TRANSMEMBRANARES

#Usando o Phobius, diz que tem (ver imagens)

#Usando o TMHMM, diz que está (ver imagens)


#MODIFICAÇÕES PÓS TRADUÇÃO

