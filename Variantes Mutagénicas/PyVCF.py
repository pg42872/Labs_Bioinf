import vcf


portuguesa = vcf.Reader(open('C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Aula_TBL/dados/trimmomatic/ERR4157959.raw.vcf', 'r'))
for record in portuguesa:
    print(record)
    
espanhola = vcf.Reader(open('C:/Users/Zé Freitas/Desktop/Mestrado/Labs_Bioinf/Aula_TBL/dados/trimmomatic/ERR4395294.raw.vcf', 'r'))
for record in espanhola:
    print(record)