from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import Entrez

#PHB
#Aceder ao NCBI e importar o ficheiro do gene no formato GenBank
Entrez.email = "jpsfreitas12@gmial.com"  # Always tell NCBI who you are
handle = Entrez.efetch(db="nucleotide", id="NC_000017.11", rettype="gb", retmode="text")
print(handle.read())

#Ficheiro FASTA
phbfa = SeqIO.read(open("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/PHB/sequence.fasta"),"fasta")
phbfa

my_seq = Seq("GCAGTATGTGTGGTTGGGGAATTCATGTGGAGGTCAGAGTGGAAGCAGGTGAGAATGGAGGGGGCGGCAAAGGCTCGTTTCTGGGCATCTCTGCAGTCCTCCTCTGCTCCATGATGTGCACTTTGGGCGAGGAGAGTGCGTGCGTGAGTCCGACTTGTGAGGGAGGGGAGAAGGGGCTGAGCCCGGGACGAGCCAGGGGTTGCTCAGAGTAAGGGAGGTGTCCATGGAGGCAGGGTGAGGAATAATCCAGAAGCTATTACAAATGTAAAGGGCCGGGTGTCCCAGCCTCAGAGAAGGAAGATTTAAATGCACTGGACGAGATCAGGGTAGTCTCAGGAGTTGAGGTCTGGGAAGTAGGGAGGGAGGATTTGAGACTGGAGCGGGCAACGACGGTGGGGCGGAGCGTTAGAAAGTTACATGCTGGCGTGATTTCTAGTTAGGTCAACTGTGCTTATGCCCACCCCGCCTCAGCCCCACCCTCCCAGTTATTCCAGAGCTCACTGTCCCTGTGCAGCTAGTTAGAGCCTTTCTCCCAAATGGGTTCTTCAGTTATCTTGGCCCCAGGATGTCATCCAGCTCCTGCTTCCATAAGAAGCATGTCGTTCTTAATACACGATGTTGACAAGCAGTATGGTGAGGAGGTAAGCTGTGTCTGCTAGCATTAGACCTCTGGGTTCTAATTCTGGTTCTACCACTTAATAACTGCAATCTCGGCTTCTCATGTAACCTCTCTGTGTGCCTCTGTTTCCTCTGTAGTAATATGCTTCATAGGGTAATTGTGAGAAGTAAATAAATTGCTTTTATTAGGCTACCTGATATAAGTGTTAGCTGTTACGGTTACTTTTTTTGTTGGCATCAACATGTAGCACATTTTTTAAGTTATTTTTTTCAAACCATAATTGCACCAATCTAACCTCACAGCCTCTTTTTGGGGGCCTACTTGTCCAGGAAATGAGAGGGTGGTTTAGTGTGGTGCTAAGTTCTCTGTGGATTTCAAGCCCATGCATTGTTTTCATTATTGAACCAAGTGTCCCAGACACCTTACTTTAAATGGTTGAGAAAAAAAGAGAAATCAGCCAGGCATGATGGCTCATGCCTGTAATCCCAACACTTGGGAGGCCGAGGCAGGGGGATCACTTGAGCCCAGGAGTTTGAGACCACCTGGGGCAACGTAGCAAGACCCCATCTCTGCAAAAAATGAACAAAATTAGCCGGGCATGGTGGCACACTTCTGTGGTCCCAGCTACTTGGGAGGTTGAGGTGAGAAGATCGCTTGAGCCTGGGAGGTCGAGGCTTCAGTGAGCTGAGATTGCACCACTGCACTCCAGCCTGGGTGACAGAGCAAGACCCTGTCTCCAAAAAAAAAAAAAGGAAAGAAAAGAAACTGAAAAAAAAAAAAAGCAGAAGAATTGATAGTACACTTTCCAAGCTATAAAGCATTATTTATTAGGTATCCTTCAATGGATGATTTAGCACTTTCAGGAATGGGGAAATAAATAGCCAGGTTGAAAAGTGACTGTTGTGTGTCAGAGAGGGCCTTCTCTGAGGATTTGGCATCAAGTTTGATTGTATTTTGTTTTTATCCCCTTAGGTGTGAGAGGGTCCAGCAGAAGGAAACATGGCTGCCAAAGTGTTTGAGTCCATTGGCAAGTTTGGCCTGGCCTTAGCTGTTGCAGGAGGCGTGGTGAACTCTGCCTTATATAATGGTGAGGCATGGAGGGACAGTGGGTCACTGCACTTTCCTAGGAGTTTTCTGTTGGTCTGCATAGCCCATGTGACACTCTTGATGGTAGCTGCCGTCAGTGAATGTGTTTGTGGCCAAGAGGGCTCACCTCCTGCCATTTCATACCACAGGACTGCATTGTTATCAGAGCCCCTGACCTTTCAGTCATAGGTTCTCTCAGAGCCTGTATTCAAAAAGAGCTTCCCAGCCCACTTCCTAGTTGGATGTGTCCAGTGGCTTCTGTCAAGGTGAAGTGAAGCCGCACCACCCAAATGCTGCCGCACAGTGTCTGGATTTCCCTGGCTATCTGAAATGGAGATCTCATTTGTTCTCCTCTGCTTGCATGTGGAATAACAGCAAAGGCTGCAGATCTGTTTGGGTGACCTTGTCCTGAACAGGAACTTTTGCTGTGCTGAATTCGGGTAGTTTCAGAGAAAGTATCTTTGAGATGCATTGCCCAGCTTTTAACAGTGTAGGAGGGAGGTTAAGCTGGCTTTTCTTCCACTTTACTGTGGAAGCTTCCTCATTGGTCAAGCAATGGATTTGACCTGACTTTATCTGTAGGACCTCCTTTAATTCTGACATTCTGACACTTTCACATGCTGCAAAGCAGCAATAGATTGACCCATCCGGTGTGTGGCTGGCTGACAAGAGGAGCTTTACTTTCAGAGTGAAGATATTTGGACCAATGATAAAGTTCAGAGAGGCAGCTGATTAGAAAAGCCTGCTTGGCTTATATGACACATCTTAGCAGTACTGTGATCCTTTTGGCCACATCTGCAACTAGACAGAAATTGCCATCATAAATTTCTCTCTGTGCCAAGACAGCTCTATAACCCCTTAAAACTTTAGCGAAACAGAGCTATTAGGAAGAAAGAGTAGGCTCTTCGAAATGTAGGATTCCCATAATGAGGGTGCTACTTCTGGGAGCACTAGGTTAAATTGGAGCCCGATGGATATGTGGTAACTGGGAAGACCTCACTGAGTTTTAGAAGTTTTGGTAGATGATTCCTGGAAATATGTTGGTGGGAGTTCAGGGATAGAATGGTCATTCAGAAAATCAACAGCCAGTTCCCTCAAGGAGAAAGGATGCTAAGGAACAGGTCCTATTACCAATCCTTGGGGACATGTGGAACAGGAAGTGACTGCTTAGTTTTGCAGCTAGTTAGAAGTCTCTAGAGACCAGGAGTTGGGGAAGACAGAGAGAAGAGGGGAGACTTAATAAGTGAACAGAAAGCACCAGGGCTCTTTCAAAGACATGATCCTTTTGTTTAAAGGATGAGAGGATTTTTATGACATGTCATTGTCCTTTCTTCCTAGTGGATGCTGGGCACAGAGCTGTCATCTTTGACCGATTCCGTGGAGTGCAGGACATTGTGGTAGGGGAAGGGACTCATTTTCTCATCCCGTGGGTACAGAAACCAATTATCTTTGACTGCCGTTCTCGACCACGTAATGTGCCAGTCATCACTGGTAGCAAAGGTGAGTCTTGCCTATGGTTCAGGTAAAGTAGGGAGTGTGGAAGAGGTGCTCTGTTCTTCTGTGTCACAGGAGCATCTGTGGGATACCAGGATCCAAAAGAGTTTGAACTGTACATCATAGGAATGACTAGACTACTTGCCCTGGAGAGCTTGATATGGAATCTTAGAAATACCCACTTATGGCTGGGTGCGGTGGTTCATGCCTGTAATCCCAGCACTTTGGGAGGCTGAGGCAGGTGGATCACCTGAGGTCAGGAGTTCAAGACCAGCCTGGCCAATGTGGTGAAACCCCATCTCTCCTAAAAATACAAAAATTAGCCGGTGGTGGGGGGTGCCTGTAATCCCAGCTACTTGAGAGGCTGAGGCAGGAGAATTGCTTGAGCCTGGGGGGCGGAGGTTGCAGTGAGCTAAGATTGTGCCACTTCACTGCAGCCTGGGCAACAGAGTGAGACTCTGTCTCAAAAAAAAAAAAAAAAAAAGCCTGCTTCTAATCTTCCCATCTCTTTGGAATTTCTTTCCGTACTGTTTTGCAGTTGTTTTCAGGATACATTATGTACCTATTTCTAAAACTATTGATAGGAGCTTCCAGAGATCAGGGAGTTGTAGGTATTAATACATTGCCCACCTCTCTTGGTGCCCAGTTCAGGGCTGTCTCATGGGCGCTTGGTCCATATTGTTGACATCTGTAAGCAAGCCGTGACAGTGCTTTGGCTCCAGGCAGGCCTGAATTGTCCAGGGGAAAGTATAATTCTCTCCCTGGATCCTTTAAATGGTCCAAGTAATGAGAAGCAGAACATAGGATCAGTCTGTTAACCCCTTATATGTGTTACACATTTGACAGAGTGCTTTTACGTCTGTTTTCTCCTTCAATTTTCCCCAACATTTCCGCAAGGCCCAGAAAGCAAATGAAATTGTCCCCATTCTCATAGACAGGGAAATAAGCTCAGGTTGGCTAAGGCTTAGAGAGGCCACATCATTAGTAAATAGCCCAGATCTTTGGACTGATAGTCTAACACCGTTTCCACCAGACCCGAACTAACCTCTCCAAGGCTGACTCCTGACTTGGCCACAATCACCAGAGCATGTAAAGGCCTCACCCTACAATTCTTAGCATTGCCCTGTCTATTGTCTTAAAATGTTCAGTGTTGCAAACTTTGCATGGCACCTGTTAGACATATAATCTGAATTATGTATATCTGAGGGCATTCAGGGGATACCAAAAAGCTGCTATCACTGAAGCCTCTTAAGAAATTATAAACTCTTTATGATGCTCTATTGGGTTCTCTGCCAAGGAAACCAGGCATACCTGCACCTTGCCCTCTGGGATCTTATAATCAGCAGATTTGCTTATAAATTGTAGCAAATTTGGAGCCAGGCACAGTGGTGCGTGTCAGCTACTCAAGAGGCTGAGGCAGGAGAAATGCTTAAGCTCAGGAGCTTGAGTCTAGCCTGGGCCACATAGCAAGACCTTGTCTCTAAAAATAAAAAATAAAAATTGCCAGGCGTAATGGCTCACACCTGTAATTCTAGCATTTTGGGAGGCTGAGGCAGTTGGATCACTTGAGCCCAGGAGTTTGAGACCAGCCTGGGAAATATGGCGAAACCCCAGCTCTACAAAAAGTACAGAGATTAGCTGGGCGTGGTGGTCTGTGCCTGTGTAGTCCCAGCTACTTGGAAGGTGTAGGTGGGAGGATCAACTGAGCCCAGGAGGTCAAAGCGGCTACAGTGAGCTGTGATCTTACCACTGCACTTCAGCCTGGGCAACATGTGACCCTGTCTCAAAATACATAAATAAAAATTGTAGCAAATTGGAGTAGGAGAGGTCATATAAAAGACCACTTGTGGCCAGGTGCGGTGGCTCACACCTGTAATCCCAGCACTTTGGGAGGCTGAGGCAGGTAGATCACCTGAGGTCAGGAGTTTGAGACCAGCCTAACATGGTGACACCCTGTCTCTACTAAAAATACAAAACAGCTGGGTGTGGCGGCGCGTGCCTGTAATCCCAGCTACTCAGGAGGCTGAGGCAGGAGAATTGCTTGAATCTGGGAGGCAGAGGTTGTAGTGAGCCGAGATTGTCCCATTGTACTCCAGCCTAGGCAACAAGAGCAAAAACCTGTCTCAAAAAAAAAAAAAAACAAAAAAAAAACACTTGTTTTCCTACAGTGGTTTTTATTTTTAACTCCAGTGTTTGTCCCCTACCCTAAGATTTACAGAATGTCAACATCACACTGCGCATCCTCTTCCGGCCTGTCGCCAGCCAGCTTCCTCGCATCTTCACCAGCATCGGAGAGGACTATGATGAGCGTGTGCTGCCGTCCATCACAACTGAGATCCTCAAGTCAGTGGTGGTGAGTGAACAGGGGCCTTTAGCCTCGAGCCCAGAGCACCACCCTGGGAGGGTGCCAGGTGGCAGGAAGCGCTTGGCAGTGGGTTGGTTGGGATGTGGCTGCTAGTTTCCTGGTTCCTTTTCTGCTTCCTCATTAACCTGACCTGCCCTTCTGCTCCTCCCTTTGAAACCAGGCTCGCTTTGATGCTGGAGAACTAATCACCCAGAGAGAGCTGGTCTCCAGGCAGGTGAGCGACGACCTTACAGAGCGAGCCGCCACCTTTGGGCTCATCCTGGATGACGTGTCCTTGGTAAGATCCTTCGGGAGACCGAGGAGGGGAAGGGGCTGCAGTTCTCGTTTAGGTGCCTGGCTCCATTTCTGGGTAGACGCTATTAGGTCCTCCCTTCTGCTTTGCTAGATGTGAGACTTGAAAACACGGAAACATGCTGAGGTGAGGCAGTCTCCGTGGGTTTTTCAGTTGAGGGTTCTTTTACCTTCCCCCTGCCACACACATTTTTCTTATGACCTCTGGTTGTATCCAGATAGTCTCTAACCACTAAATGTTTTACCTTCTCCAAACTGTTACCCAGAGAGTGATGCCTTGTTAACCCTGTTTGACACAGGCAGAAACTGCCTGGTAGAGACCAGAGAACAGCTCGGGTAGTCCTTCTCCCTAGCACAGACCTCCCAGCCTGACTCCTGGGAGCTTCCTAACACTTTACAGTCCGAAGCTCAGTGAAGTAAGCTCTGGGAACCCCAGTGAAAGGTGATAGAGTGTAAACGAACGGTTGGATTCCCCCAGGCCTGGTATAGGGGGCAAGGGACATCTCTGAGGCGTAAGCTATCCTCTTGAGACACTATAGCTTGTGTGTTTATATGACATTGGATGTCATAACTCAGAAAGCAATGCAGGCAGGATAGCGTTTCAGGTTGAGGAGGGTGAGGGGAAGGGGTCGTGTTTCTAGATTCTCTGGGAAAAACCATTTGGAGTGATTTGTTCGGGCAGTGAGGTAAAGTGTTTCCTGTTCAGTTCTCCCGTGCATTGCTAGGGAAAGGCACTGCCTCCCCCGGCATCTGTGCAGCTGTTTAAACAGCCACTTGACAACACCCAGTGCTAACCCCTGGGCACTGCTCCACCTTGCTCCGCCTGCTGGAAGTCCTGGGGGCTTGGGGCTCCCTCTGCTGGCAAGAGGCCAGGCTGCAGCCATTCTGTGGGCCCTTCCCTCGTAATTACCGTTAACCTGAACACCTTGGCTGTGAGAAAACGCTGAGTAAAAACCTAAGGGAAAAGTTGGCATTTTACTAGACTTTAACCACATACTCCATTCTGGGGAAATGTGGGCTGACCACAAGAAACCCTATCTAAGGTGTGAGAAGAAAATTAGGTTTCATGGGGAATTTGCTGCCCTCAGCTGGCCCTTGTAGAAATAAATTTTATTCCTTAATTATACATTTCATTTTTCATGTCTCAGGATCAGATTTTCTTACCCAAACTTTGACTAAGAAACTAGAAATGGATCAGGCGAAGTACAACAGCTGCAGTTAGAGTTAGGAGGTTAAAAATTCTGGAAGAGAATGAGACCAGGATTTACTCTTCAGGAGAAGTTTGGAGCTGCTTTTTTAAAAAGCAGAGGTTGGGAGAGTGGAGGAAATGAAACAACTAGAATTTGATGGCAAAACCAATGCTCTTCTCTTGATTCTTTTTCAATAAAAATTAGGATGAATAAGTAAATTGCTCTAGGCTGGGCATTAGGAATTCTGAGGTCCCTTCCCATTGTTTGTGCTATCTTTAGGGACAGTCCCGTCAGACCTGACATGATTAGGGAAGGTCTATGGATCATCAGACTTCTAAACCCTCATGCCGACCAATGACTTTACCTGCTTTCTCTTTCTTTTAAACCGTTTAACAGAACCATTCACATTGGGAATACCATGATTTGCGTTCCACCGTCCCTCGTCCTCTTCCTGTTCAGTGGTGGAGCTGCTGTGGGAAGACGCGGACTGGTTAATCCATAAACAGAGAGCATCAGGCTCTTGGATCCCTGGGAACCAGCTGCCTCCCTCACTCTCAGGGACCCTGTTTTCCATCTGGCCTTCCTTGGGCTTTGAACAAGGCATCAAAGGCCCTTGGAAGAGCACTAGTCAGTGGCGGGGGTCTTAGAACCCACAGTTCTCCTCCTCTGGGGAGGTGGTCGATTGAGTAGATACCTTCTGGTGCCTGTGGGCCCCATCAAAAGCCCCCGGTGCCATTTGCTACATGAGGTCACTGTACTGAGAGTGACAGAGTAATATACAGGAGCAGTTTGGGCAGCCAGAGAGTCTGGGTGTAAACTCAGTTTGGATACAGATACGGAGGTGGAAGAGTGTTCTGGCCTCACGGATGCCTCCAGCTGCTAGAGCCATTGCTGGCCTCTTCTTCCAGCGGCCATGGAGCCCTCCCAGCAGTGCTGTCGAAGCAATCACACTGCCTCATCTTGTGCTCACTCTCTCCCCTTAGACACATCTGACCTTCGGGAAGGAGTTCACAGAAGCGGTGGAAGCCAAACAGGTGGCTCAGCAGGAAGCAGAGAGGGCCAGATTTGTGGTGGAAAAGGTGAGCCTTCGACCAGATGGCAGGAGCCTCTCTCTCCCCTTTCTCCGGCACTCAGCTTCCCCATTTGCTGGGTGGCCTGGAAATTCATCATCTGTCATCCCTTCTTCCGGGATAATCAGAAGGGGCTTGAAGGAATTGTACTTCTGCAATTGGTTCCAGAGTCTTCAGGGGCTAGTCAAGGATATGTGGAGTTATGTTCCTAAATCACTGAAGGGTAATTTTTCTTCCACTTCTCTGAGATCAAAAACACTCTCTTACAAATAAAAATGTTTCTCCTGGAGTATTTTCAGCTTCACTGAGAAGTCATTTTTAACCATAGTTACATAGTGAAAGCTGACAGCAAAAAAGATCAAACGTTGCACCAGATGTGCTTTCGTCACTAGATTTTTTTCTAGTGCTAAATCCATCCAGATGTGTCAAAGAATGTGATGGGACACAGTGTATTTGCGTAGCAGCCTGGTCTTTCTGGTATTTGCAAAGACATGTTCATTTATTGTTGTCCCCTTCTTCCCACCACCAGTATCCCTAATTGGTGGGGAGATGGGGACAGCAAGAAATAAAATGGGAAAAGAGGGATAGATTTAATTTTGGAGAATGAAAACACTGTGTGGGCAGAGACTTGTGTTGCTTTGTATCTGCCATAACTTCAGAGATTATAATAAGTCTAGTACAGTGCCTGGTGATAGTAGGTATACAGTAAATGTTTGTTGAGCAAATAGACGCAGGGCCCAGTCATTTCAAAATTGTATGTAATTTCAGGGAGGCTTAATACTGTCTTCTTCCTCACACTCCTGAAGGTCACACGTTGCAGAGAGCTGTCTTCCTATTGATATTGGTAGGGCAAGCCTAGGAGATCTCACTCTGGGTGCCTGGATTCTGGTCAGGAACCAGCCTAACTCACAGGCAGCTCTAGGAACAGTCAAAAGTGCATGCTGCTCTTCCTTAGCCATCCCGAGGTTTTTTGTTTGTTTGTTTGTTTGTTTGTTTGTTTGTGACAGCTCTGTGGCCCAGGCTGGAGTGCAATGGCATGATCATAGCTCACTGCAGCCTTGGCCTCCTGGGCTCAAGTGATCCTCCTGCCTCCGCCTCCCAAAGTGCCAGGATTACAGGCATGAGCCACCACACCCGGCCCTGTCCTGGCTTTGATGAAGTCCTTTAGACTTAAGGCTGGAGGAAAAGATGAGCCTTGAGGATTGATTCCACCTTTCTTTTGCTTCTGTTTTCCTTGGCCTTGGCTTCTCCTGGCTCAGAGTAGGGTTGTTAAACTAGATTGCAATTAATATTAATGAGGACTTTGAAATAAGACAAATATTCCTGCAGCCAACAGAGATGTATCCCTCCCGTGACAAGGAGTGAGCATGAAAGGATAGGGGAGGACTGGTGGGCAATGTGCTCTGCTTCCCCCCGCTTCCCCCGCTAGCCATCAGGAGGAAGTAAACTCCCCGAGTTCCTTCAGGAGCCTGGGAAGGTGGCTTTCTGGTGAAGGGCCTTTGGTTGTAGCCTGACATGCGGTGCCCTGAGGTTTGATCTTTGTCTCCACCTCCATTCTTTTAGGCTGAGCAACAGAAAAAGGCGGCCATCATCTCTGCTGAGGGCGACTCCAAGGCAGCTGAGCTGATTGCCAACTCACTGGCCACTGCAGGGGATGGCCTGATCGAGCTGCGCAAGCTGGAAGCTGCAGAGGACATCGCGTACCAGCTCTCACGCTCTCGGAACATCACCTACCTGCCAGCGGGGCAGTCCGTGCTCCTCCAGCTGCCCCAGTGAGGGCCCACCCTGCCTGCACCTCCGCGGGCTGACTGGGCCACAGCCCCGATGATTCTTAACACAGCCTTCCTTCTGCTCCCACCCCAGAAATCACTGTGAAATTTCATGATTGGCTTAAAGTGAAGGAAATAAAGGTAAAATCACTTCAGATCTCTAATTAGTCTATCAAATGAAACTCTTTCATTCTTCTCACATCCATCTACTTTTTTATCCACCTCCCTACCAAAAATTGCCAAGTGCCTATGCAAACCAGCTTTAGGTCCCAATTCGGGGCCTGCTGGAGTTCCGGCCTGGGCACCAGCATTTGGCAGCACGCAGGCGGGGCAGTATGTGATGGACTGGGGAGCACAGGTGTCTGCCTAGATCCACGTGTGGCCTCCGTCCTGTCACTGATGGAAGGTTTGCGGATGAGGGCATGTGCGGCTGAACTGAGAAGGCAGGCCTCCGTCTTCCCAGCGGTTCCTGTGCAGATGCTGCTGAAGAGAGGTGCCGGGGAGGGGCAGAGAGGAAGTGGTCTGTCTGTTACCATAAGTCTGATTCTCTTTAACTGTGTGACCAGCGGAAACAGGTGTGTGTGAACTGGGCACAGATTGAAGAATCTGCCCCTGTTGAGGTGGGTGGGCCTGACTGTTGCCCCCCAGGGTCCTAAAACTTGGATGGACTTGTATAGTGAGAGAGGAGGCCTGGACCGAGATGTGAGTCCTGTTGAAGACTTCCTCTCTACCCCCCACCTTGGTCCCTCTCAGATACCCAGTGGAATTCCAACTTGAAGGATTGCATCCTGCTGGGGCTGAACATGCCTGCCAAAGACGTGTCCGACCTACGTTCCTGGCCCCCTCATTCAGAGACTGCCCTTCTCACGGGCTCTATGCCTGCACTGGGAAGGAAACAAATGTGTATAAACTGCTGTCAATAAATGACACCCAGACCTTCCGGCTCA")
print(my_seq)
tamanho_seq = len(my_seq)
print(tamanho_seq)

#Percentagem de cada nucleótido na sequencia
A = (my_seq.count("A")/len(my_seq))*100
print("A: ",A)
T = (my_seq.count("T")/len(my_seq))*100
print("T: ",T)
G = (my_seq.count("G")/len(my_seq))*100
print("G: ",G)
C = (my_seq.count("C")/len(my_seq))*100
print("C: ",C)

#Ficheiro GenBank
phbgb = SeqIO.read("C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/PHB/sequence.gb","genbank")
phbgb

id = phbgb.id
id
ano = phbgb.annotations
ano
organismo = phbgb.annotations["organism"]
organismo
taxonomia = phbgb.annotations["taxonomy"]
taxonomia

#Listagem de features
for feat in phbgb.features:
    print(feat)

#Listagem de features relevantes para a codificação da proteina
for feat in phbgb.features:
    if feat.type == "source" or feat.type == "gene" or feat.type == "CDS":
        print(feat)

#BLAST de nucleotidos, usando a base de dados nt
blast = NCBIWWW.qblast("blastn", "nt", phbfa.format("fasta"))

save_file = open("my_blast_phb.xml","w")
save_file.write(blast.read())
save_file.close()
blast.close()

#leitura dos resultados obtidos do BLASTn
result = open("my_blast_phb.xml")
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