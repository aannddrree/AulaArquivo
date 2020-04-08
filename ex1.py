arquivo = open('c:\\tmp\\dados.csv', 'r')
arquivo_output = open('c:\\tmp\\output.csv', 'w')

lines = arquivo.readlines()

print("Inicio do processamento")

nomes = []
telefones = []

try:
    for l in lines:
        colunas = l.split(';')
        nomes.append(colunas[1])
        telefones.append(colunas[2])
except:
    print('Posição inválida')

qtdElementosLista = len(nomes)
qtdElementosLista = qtdElementosLista - 1
print("Quantidade de registros da lista: " + str(qtdElementosLista))

i = 1

lista_saida = []

while i <= qtdElementosLista:
    lista_saida.append("O nome da pessoa é " + nomes[i] + " e o telefone é " + telefones[i])
    i = i + 1

arquivo_output.writelines(lista_saida)

arquivo_output.close()
arquivo.close()
print("Fim do processamento")