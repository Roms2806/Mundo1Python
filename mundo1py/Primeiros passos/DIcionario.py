#tipo de mapeamento
#dict = dicionário
mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
print(type(mydic))

#acesso a itens do dict

mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
print(mydic["nome"])
x = mydic["altura"]
print(x)
z = mydic.get("year")
print(z)
#diferentes formas de acessar um item do dicionário
c = mydic.keys() #lista de chaves visualização do dicionário
c1 = mydic.values() #lista de valores
print(c,c1)