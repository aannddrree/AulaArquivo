arquivo = open('c:\\tmp\\dados.csv', 'r')

lines = arquivo.readlines()

for l in lines:
    if "André" in l:
        print(l)
