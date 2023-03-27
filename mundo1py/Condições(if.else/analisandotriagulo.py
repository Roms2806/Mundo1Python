print('=' * 20)
print('Analisando um triângulo...')
print('=' * 20)
s1 = float(input('Primento segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmento podem formar um triângulo')
else:
    print('Os segmento não podem formar triângulo')