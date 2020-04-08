arquivo = open('c:\\tmp\\saida10.csv', 'w')

lista = ['nome;telefone;endereco', 'andre;123455;rua1', 'luiz;234234;rua2']

lst_saida = []

for l in lista:
    coluna = l.split(';')
    lst_saida.append(coluna[0] + ';' + coluna[1] + '\n')

arquivo.writelines(lst_saida)

