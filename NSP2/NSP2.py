from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SwissProt
from urllib.request import urlopen
from Bio.Align.Applications import ClustalwCommandline, MuscleCommandline
from Bio import AlignIO
from Bio import Phylo

#NSP2

nsp2 = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/nsp2.fasta"),"fasta")
nsp2
###não é possivel download do ficheiro genbank

#Abrir ficheiro SwissProt localmente FASTA
ficheiro = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/M20210105A94466D2655679D1FD8953E075198DA82BA1B88.fasta"),"fasta")
ficheiro 

#Abrir ficheiro SwissProt localmente full infor
ficheiro = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/uniprot-yourlist_M20210102E5A08BB0B2D1C45B0C7BC3B55FD265560A91A6U.txt")
ficheiro

record = SwissProt.read(ficheiro)
print(record.description)
print(record.references)

for ref in record.references:
    print("authors:", ref.authors)
    print("title:", ref.title)
    print(record.organism_classification)

#Abrir ficheiro SwissProt pela internet
url = "https://www.uniprot.org/uniprot/P0DTC1.txt"
handle = urlopen(url)
handle 

recorde = SwissProt.read(handle)
recorde
print(recorde.description)
print(recorde.references)

#BLAST de proteinas 
blast = NCBIWWW.qblast("blastp", "nr", nsp2.format("fasta"))

save_file = open("my_blast_nsp2.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()

#Leitura dos resultados do BLASTp (ficheiro obtido pelo BLAST na web, bd = SwissProt)
result = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/NSP2_alignment_SWISS.xml")
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

#Leitura dos resultados do BLASTp (ficheiro obtido pelo BLAST na web, bd = nr)
result = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/NSP2_alignment_nr.xml")
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
cline = ClustalwCommandline("clustalw2", infile="C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/NSP2_MA.fasta")
print(cline)

cline = MuscleCommandline(input="C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/NSP2_MA.fasta", out="NSP2align.aln", clw=True)
print(cline)

#Leitura de ficheiro do alinhamento multiplo
alignment = AlignIO.read("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/NSP2alinhados.fasta", "fasta")
print(alignment)


#Leitura do ficheiro da arvore filogenética
arvore = Phylo.read("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/NSP2/NSP2arvore.dnd", "newick")
print(arvore)

Phylo.draw_ascii(arvore)
