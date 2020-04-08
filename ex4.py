
def is_nome_frase(nome_completo, sobrenome):
    if sobrenome in nome_completo.lower():
        resultado = 'SIM - o nome {} está na frase'.format(sobrenome)
    else:
        resultado = 'NAO - o nome {} está não na frase'.format(sobrenome)
    return resultado

nome_completo = str(input('Qual é o seu nome completo: ')).strip()
print(is_nome_frase(nome_completo, 'silva'))
print(is_nome_frase(nome_completo, 'gomes'))

#print('teste {} %%% teste aaaa {}'.format('1','2'))