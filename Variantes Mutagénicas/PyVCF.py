import vcf
from BCBio import GFF

portuguesa = vcf.Reader(open('C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Variantes Mutagénicas/ERR4157959.raw.vcf', 'r'))
for record in portuguesa:
    print(record)
    
espanhola = vcf.Reader(open('C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Trabalho prático/scripts/Labs_Bioinf/Variantes Mutagénicas/ERR4395294.raw.vcf', 'r'))
for record in espanhola:
    print(record)
    