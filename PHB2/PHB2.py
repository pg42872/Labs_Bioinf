from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import Entrez
from Bio.Align.Applications import ClustalwCommandline, MuscleCommandline
from Bio import AlignIO
from Bio import Phylo


#PHB2
#Aceder ao NCBI e importar o ficheiro do gene no formato GenBank
Entrez.email = "jpsfreitas12@gmial.com"  # Always tell NCBI who you are
handle = Entrez.efetch(db="nucleotide", id="NC_000017.11", rettype="gb", retmode="text")
print(handle.read())

#Ficheiro FASTA
phb2fa = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/PHB2/sequence.fasta"),"fasta")
phb2fa

my_seq = Seq("TCCGTATGCGCGATTCCT.....GTGCGCGAAGTTCGGGTCCGTAGTGGGCTAAGGGGGAGGGTTTCAAAGGGAGCGCACTTCCGCTGCCCTTTCTTTCGCCAGCCTTACGGGCCCGAACCCTCGTGTGAAGGGTGCAGTACCTAAGCCGGAGCGGGGTAGAGGCGGGCCGGCACCCCCTTCTGACCTCCAGTGCCGCCGGCCTCAAGATCAGACATGGCCCAGAACTTGAAGGACTTGGCGGGACGGCTGCCCGCCGGGCCCCGGGGCATGGGCACGGCCCTGAAGCTGTTGCTGGGGGCCGGCGCCGTGGCCTACGGTGTGCGCGAATCTGTGTTCACCGGTGAGCAACCTCCGCCTGCTCGCCGGACGCTTCCAGTCCCTCCCCCAAACCCCTTGCCCTGTCCCCGCGCCCCTCCACGGGCCTAGCATTTCCTCTGAGCAGCGGCCTGGCCTGATCACCACCCATCTCCCCACAGTGGAAGGCGGGCACAGAGCCATCTTCTTCAATCGGATCGGTGGAGTGCAGCAGGACACTATCCTGGCCGAGGGCCTTCACTTCAGGTAATGGCGGGCAGAGCCTGCTGACCCTGACCTTTCACCCTTGACGCCGACCCAGCAGTGGCTATAGTCGGACGTGCAACAGGATTCAACGCTGCTCTTTTCCCACCCTCCTCATCCCTGCCCCTAGGATAGTGGGTGCTGCGAGAACCTCCAGCAGCATACAAACTGTTGTTTTCCAGAGGGACAAGAGAATCTCTCCTTGTCTGTGGTCGTGGAGAGGAGCAGGCCAAAAAACGCGTGGTGAGGGGAAACCGGGCAAGGCTAGTGAAACTGCGGCCTTTTCTTTTTTTTTTTTTGGAGAGGGAGTCTTGCTCTGTCGCCCAGGCTGGAGTGCAGTGGCGCGATCTCGGCTCACTGCAACCTCCGCCTCCTGATTTCAAGCGATTCTCCTGCCTCAGCCTCACGAGTAGCTGGGATTACAGGCGCCCGCCACCACGCCCGGCTAATTTTTGTATTTTAGTAGAGACGGGGTTTCACTATGTAGATCAAGCTGGTCTCGAACTCCTGACCTCAAATGATCCGCCCGCCTCGGCCTCCCAAAGTGCTGGGATTACAGGCGTGAGCCACCGCGCCCGGCCGAAACTGTGGCCTCTTAATACCTATCCCTGTCCTCTCCAGGATCCCTTGGTTCCAGTACCCCATTATCTATGACATTCGGGCCAGACCTCGAAAAATCTCCTCCCCTACAGGCTCCAAAGGTAGGTCTGAGCACTTGGTAATCACATGGCAGGTGGGATGATCAAGGTAGCTGGCAAGAAACCCCAGGGGAATATGGTAGTGTCAGGCCTTTAGGCCTCTTTCCACATCTGCAAGAGCTGTAACAAAAATACCTGCCTCCTGGGGTCAAAGCAGCAAATTCTGAACACACTGTGTTTGCGTGCTTTTTACTGTCTCCTCCCTGACGTGTATTCAATAAGAGTATTGTTTGTCCCTCGTCTTGTTCACTGCCTAGATCAAAGCTTTGTTTTAAAGCCTTTTTTTTCTAACTGCTTGACTTACTATATCTACAGTTACATCCACTAGTACACTCTGTTCTGGAGAAGTTTGTCCCTAAGCTTGACTAGTTCACCTGTTCTCTCCTTCTAGACCATACATAAAAGCCGTGCCTTTGAGTTCCCCAGACCTCTTCCTCCTCCCCACCCACGCACACATATACACCCTGGGTCAGGTAGCTCACCTGTAACCTGTAATGTACTTCTTTGTGCTATACCTAGTGCAGGTCGCTTATTCATTTACTAGACTGGGCCCTGGGAATAAAAGATTCATTAAACACAATTCTTGTCCCCCAAGTCCTTACAGGAGACATGATTACGGTACAGCACGAAAGCGCCCACGTTAGAGGTTGCACAGAGTACAGAGGGGGAAAGAGTAGTCAGCTCTGCTGGTGACGGGGTTTGCAGTTCAAGGCTTCACAGTGGGTGAGGGTGCATTTCAGCTGTGCTGCGTCTTGTCTTCCTTGTCAGCCTGATTAACTCTCCTCCCCCCAGGGTAGTGCCAGGCTGTACACCATTGCACAGGGCATACAGGGAGGAACATGAAGGAGAAAATGCTTGGGAAAGGGTGTTTGGCCTTGACCAGCCACTGCTGACCTCAATCTCAGACCTACAGATGGTGAATATCTCCCTGCGAGTGTTGTCTCGACCCAATGCTCAGGAGCTTCCTAGCATGTACCAGCGCCTAGGGCTGGACTACGAGGAACGAGTGTTGCCGTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAATGCCTCACAGCTGATCACCCAGCGGGCCCAGGTCTGACTCCCACCACCATCTGCGTGGTGTCAGCCTTTCCTTCCTAGGCCCAGAGTATTGGGAATTAGGAAAGGCAGCTTATTAGAAAAGCATTGTCACCCTAGTGCCATTTCCACCTAAAAGCTGTGCTAATTGCCACTGTGAAATAAGGAGAGCCAGCATTAGAACTCGATAGCACTCGGTGTTAGGAAGCACAGAGGAAAATGGCCAAGTCTTGGCTTTTCCTGCACCTCTTCGAGCAGAGAGGCTTATGTTACAGGTTTGCCTGACAGGAAGCTAAGGCAGTGCATGTTGTATTGAGAGTGAAGGGTTAGGGGTCGCAACCTTCCTTTCAGCTCCCCAGTCCCCTCAAACCACCCCTCCCTTCCCCTCTTCACCCCTGCCCTCAGGTATCCCTGTTGATCCGCCGGGAGCTGACAGAGAGGGCCAAGGACTTCAGCCTCATCCTGGATGATGTGGCCATCACAGAGCTGAGCTTTAGCCGAGAGTACACAGCTGCTGTAGAAGCCAAACAAGTGGGTGAGTCGCAAGAGCCGTGGGGTGAGGGCTTCTGAGATGCAGGAGGAGGAAAGACTCCATGGGTGGGGCTCCTGACCCAGGACAGGGTCTCCCTGACTCTCTCCCACCACAGCCCAGCAGGAGGCCCAGCGGGCCCAATTCTTGGTAGAAAAAGCAAAGCAGGAACAGCGGCAGAAAATTGTGCAGGCCGAGGGTGAGGCCGAGGCTGCCAAGATGATATCCTTCTGCTGGAGAGATCTCAGCCCAGCCCCTAGGGCACCTGAGTTCCCCATTCTCCTTCATGGGCAGGCTGATGAGACTAAGGCGAATGCGACTCCGTGCTCTCTGGCCCTTGGCTCCTTGTTGGGGGTGGGGACTACAGATGAGATCTGAAATCTTAGTGGTAGTACCTGAGCCATGACTCCCCACTGTAAGGCCAGATCAATAGCATTGGTGGCCTTGCCTTCATTTCTGGTGCTGCCCCTAGTTCCTGGCAGCAGCCTGCAGGGAGGCCCACAGGTGGGGTCCACGGTAGGGCTGGGCACAAGCCACCTGAGCGCAACCTTGGATCTGACAGCCCAGAGGAGGACTGGAGCAAGGGAGTGTGGTAAGGACAGGGCCAGGGATTGAGACCTGCCCTTGCGTGTACCTTAACCCTCCTCACCTTGGAGAAGCACTGAGCAAGAACCCTGGCTACATCAAACTTCGCAAGATTCGAGCAGCCCAGAATATCTCCAAGACGGTGAGTGTGTCAGCCCAGCGTCTCTGATGGGGCTGCCTTGAGAAAGTGCTTTCAGTTAAGGCACATTGAGGTGAGGGAATTCGAACCTTGCTTGTTCCGGTTTCTACTCAGATTGGCTTCTCTGGCCGGCGCGGTGGCTCACGCATGTAATCCCCGCACTTTGGGAGGCCAAGGTGGGTGGATCACCTGAGGTCAGGAGTTCGAGACCAGCCTGGCCAACATGGTGAAACCCCATCTCTACTAAAAATACAAAAGATAATGAGCCCGCTGTGGTGGCGTTTAGCTATATTCCCAGCTACGCAGGAGGCTGAGGCAGGAGAATCACTTGAACCCAGGAGGCGGAAGTTGCAGTGAGCTGAGATCATGCCACTGCACTCCAGCCTGAGCAACAGAGCAAGACTCCGTCTCAAAAATAAATAAATAAAAAATTGGCTTCTCCGATACTCCTCCTGTCAAGAATGATTCCTCTGGGTTCCCTGACCTTTTGTTCTAATCATAGCTGCTGCTCAGCGCTCTGGATCCCTAAGTGCGAGCAGAAACCATGTGTTACTCATTGCTGCACCCCTGCCCTAATCTGCATGTGTTCCATGTTAAGTAGCTGCTGAATTGCAGGGGTCGGAATTGAGGTCTTTGCTTAATGCAAGCATCTGTCTTATTTCCTGCCCTGTAGATCGCCACATCACAGAATCGTATCTATCTCACAGCTGACAACCTTGTGCTGAACCTACAGGATGAAAGTTTCACCAGGTGAGAGATGTGGCCACACTGTGGGGTATCACCAAGAACGTGGGACCTGAGTCTGGTTGTTTGGGCTCTGGAGCCTGCTACAGCTATTCATATGGCTCAGAGACATTGAACCAAAATTAGAAAAGGGGGTGGTTGACAGTTTCTATCTTGCATCTCATAGGATTGATTTTATGAGATCAAATAGGATTATTCACATAAAAAGCACTTTAATTATAAAGTTTTCATCTAACCAAAAAGTGATGAAAGATGATACTCAGTTTTCTTACTCAAGAGCCCTCAAACTCCTCTGGTGAATGGAGGGATGTTAGGAAAGGAGATGAGAAATAGCAGTGGCCATGAGAACATGCCTCCTCCTTTCATGAGCCTGAGATTCCTGGCTGTCAACCCTGTTTATCTTTTCTCTTGGGAGCAAAGGAGGGTTCAAAGCTGAGTGGGGCCTGAAGCTGTCAATTAACATGTGCATTTCTCTTCTCTGTTTCTTGTTCATCTGGCGATCTGGCACCACAGGGGAAGGTAAGCTGTTGTTGCTTCTGTGGGGTCCTGCAGGCCACCTTCTCCAGTACCCGCCTCCTACCCTACCCCCTTTCCCACCTCCCCGAAGACAAACCCTCAATCAGGGTAGGAGGGTCGTAGAGGGAATGGCCTAGAGTGTCCTGCCTCTCACATTTATGTCCCCTAATAATGTCATTATCTATCTTTTTTTTCCTACAGTGACAGCCTCATCAAGGGTAAGAAATGAGCCTAGTCACCAAGAACTCCACCCCCAGAGGAAGTGGATCTGCTTCTCCAGTTTTTGAGGAGCCAGCCAGGGGTCCAGCACAGCCCTACCCCGCCCCAGTATCATGCGATGGTCCCCCACACCGGTTCCCTGAACCCCTCTTGGATTAAGGAAGACTGAAGACTAGCCCCTTTTCTGGGGAATTACTTTCCTCCTCCCTGTGTTAACTGGGGCTGTTGGGGACAGTGCGTGATTTCTCAGTGATTTCCTACAGTGTTGTTCCCTCCCTCAAGGCTGGGAGGAGATAAACACCAACCCAGGAATTCTCAATAAATTTTTATTACTTAACCTGAAGTCAAGGCTTCACGTGTTCATGAAC")
tamanho_seq = len(my_seq)
print(tamanho_seq)

#Percentagem de cada nucleótido na sequencia
A = (my_seq.count("A")/len(my_seq))*100
T = (my_seq.count("T")/len(my_seq))*100
G = (my_seq.count("G")/len(my_seq))*100
C = (my_seq.count("C")/len(my_seq))*100

print("A: ",A)
print("T: ",T)
print("G: ",G)
print("C: ",C)

#Ficheiro GenBank
phb2gb = SeqIO.read("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/PHB2/sequence.gb","genbank")
phb2gb

#Anotações

id = phb2gb.id
anotacoes = phb2gb.annotations
tipo = phb2gb.annotations["molecule_type"]
organismo = phb2gb.annotations["organism"]
taxonomia = phb2gb.annotations["taxonomy"]

print(id)
print(tipo)
print(organismo)
print(taxonomia)

#Listagem de features
for feat in phb2gb.features:
    print(feat)

#Listagem de features relevantes para a codificação da proteina
for feat in phb2gb.features:
    if feat.type == "source" or feat.type == "gene" or feat.type == "CDS":
        print(feat)


for feat in phb2gb.features:
    if feat.type == "CDS":
        if feat.qualifiers["product"] == ["prohibitin-2 isoform 1"]:
            print(feat)
        
        
#BLAST de nucleotidos, usando a base de dados nt
blast = NCBIWWW.qblast("blastn", "nt", phb2fa.format("fasta"))

save_file = open("my_blast_phb2.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()

#leitura dos resultados obtidos do BLASTn (ficheiro obtido pelo BLAST na web)
result = open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/PHB2/PHB2_alignment.xml")
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
