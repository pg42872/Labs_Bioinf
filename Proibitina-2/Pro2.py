from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SwissProt
from urllib.request import urlopen
from Bio.Align.Applications import ClustalwCommandline, MuscleCommandline
from Bio import AlignIO
from Bio import Phylo


#Proibitina-2
#Ficheiro NCBI local

pro2 = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina-2/sequence.fasta"),"fasta")
pro2

my_seq = Seq("MAQNLKDLAGRLPAGPRGMGTALKLLLGAGAVAYGVRESVFTVEGGHRAIFFNRIGGVQQDTILAEGLHFRIPWFQYPIIYDIRARPRKISSPTGSKDLQMVNISLRVLSRPNAQELPSMYQRLGLDYEERVLPSIVNEVLKSVVAKFNASQLITQRAQVSLLIRRELTERAKDFSLILDDVAITELSFSREYTAAVEAKQVAQQEAQRAQFLVEKAKQEQRQKIVQAEGEAEAAKMLGEALSKNPGYIKLRKIRAAQNISKTIATSQNRIYLTADNLVLNLQDESFTRGSDSLIKGKK")
my_seq
tamanho = len(my_seq)
tamanho

#Abrir ficheiro SwissProt localmente FASTA
ficheiro = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina-2/uniprot-yourlist_M20210105A94466D2655679D1FD8953E075198DA82BA1F57.fasta"),"fasta")
ficheiro 

#Abrir ficheiro SwissProt localmente full infor
ficheiro = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina-2/uniprot-yourlist_M20210102A94466D2655679D1FD8953E075198DA82A5A6BY.txt")
ficheiro

record = SwissProt.read(ficheiro)
print(record.description)
print(record.references)

for ref in record.references:
    print("authors:", ref.authors)
    print("title:", ref.title)
    print(record.organism_classification)

#Abrir ficheiro SwissProt pela internet
url = "https://www.uniprot.org/uniprot/Q99623.txt"
handle = urlopen(url)
handle 

recorde = SwissProt.read(handle)
print(recorde.description)
print(recorde.references)


#BLAST de proteinas 
blast = NCBIWWW.qblast("blastp", "nr", pro2.format("fasta"))

save_file = open("my_blast_pro2.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()

#Leitura dos resultados do BLASTp (ficheiro obtido pelo BLAST na web)
result = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Proibitina-2/Pro2_alignment.xml")
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
