'''print('\33[7mRâmila\33[m')
nome = input('qual seu nome? ')
print('Prazer em te conhecer, {}{}{}!'.format('\33[4;35m', nome, '\33[m'))'''
#dicionário
nome = input('qual seu nome? ')
cores = {'pretoebranco':'\33[7m',
         'azul' : '\33[34m',
         'limpa' : '\33[m'}
print('Prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))