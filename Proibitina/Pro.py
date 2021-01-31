from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SwissProt
from urllib.request import urlopen
from Bio.SwissProt import KeyWList
from Bio.Align.Applications import ClustalwCommandline, MuscleCommandline
from Bio import AlignIO
from Bio import Phylo

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
print(len(record.references))
print(record.references)

for ref in record.references:
    print("authors:", ref.authors)
    print("title:", ref.title)
    print(record.organism_classification)

#Comentário sobre o complexo formada pela pro e pro2
print(record.comments[4])

#Artigo da interação da nsp2 do SARS-CoV com a proibitina
print(record.comments[5])
#RN   [11]
#RP   INTERACTION WITH SARS-COV NSP2 (MICROBIAL INFECTION).
#RX   PubMed=19640993; DOI=10.1128/jvi.00842-09;
#RA   Cornillez-Ty C.T., Liao L., Yates J.R., Kuhn P., Buchmeier M.J.;
#RT   "Severe acute respiratory syndrome coronavirus nonstructural protein 2
#RT   interacts with a host protein complex involved in mitochondrial biogenesis
#RT   and intracellular signaling.";
#RL   J. Virol. 83:10314-10318(2009).


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

#Leitura dos resultados do BLASTp (ficheiro obtido pelo BLAST na web)
result = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/Pro_alignment.xml")
blast_records = NCBIXML.parse(result)
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

#Alinhamento multiplo e arvore filogenética
help(ClustalwCommandline)
cline = ClustalwCommandline("clustalw2", infile="C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/Probitina_MA.fasta")
print(cline)

cline = MuscleCommandline(input="C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/Proibitina_MA.fasta", out="Proibitina_MA.aln", clw=True)
print(cline)

#Leitura de ficheiro do alinhamento multiplo
alignment = AlignIO.read("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/Proibitinalinhados.fasta", "fasta")
print(alignment)


#Leitura do ficheiro da arvore filogenética
arvore = Phylo.read("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina/Proibitinarvore.dnd", "newick")
print(arvore)

Phylo.draw_ascii(arvore)
