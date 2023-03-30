#Faça um programa que leia algo pelo teclado 
#Mostre seu tipo primitivo 
#E todas as informações possíveis

x1 = (input('digite algo: '))

print('O tipo primitivo é', type(x1))

print('Ele é alfanumerico?', x1.isalnum())
print('Ele contem apenas letras?', x1.isalpha())
print('Ele é um número?', x1.isnumeric())
print('Ele é um decimal', x1.isdecimal())
print('Todos os caracteres são caracteres?', x1.isascii())
print('Todos os caracteres são digitos?', x1.isdigit())
print('Temos letras minúsculas?', x1.islower())
print('Todos os caracteres são espaços em branco?', x1.isspace())
print('Temos letras em caixa alta?', x1.isupper())

#mais alguns métodos de strings
capitalize() #converte o 1º caracter em maiúscula
casefold() #converte strings em letras minúsculas
center() #retorna uma string centralizada
count() #retorna o nº de vezes que um valor especificado ocorre em uma string
encode() #retorna uma versão codificada da string
endswith() #retorna TRUE se a string terminar com valor espcificado
expandtabs() #define o tamanho da tabulação da string