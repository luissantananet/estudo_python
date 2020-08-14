"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com a ano atual (int)
* Obter o ano de nascimento da pessoa(daseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 cadas decimais (pesso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings(com as chaves)
"""

nome='Luis'
idade=31
altura=1.80
peso=64.0
ano_atual=2020
imc=peso /(altura**2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:0.2f}.')
print(f'{nome} nasceu em {ano_atual - idade}')
