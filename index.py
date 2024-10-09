import pandas as pd 

print("=================================================================")
print("Visualização de Dados em um Dicionário")

dic1 = {'ESTADO': ['AMAZONAS', 'AMAPÁ', 'ACRE'], 'SIGLA': ['AM', 'AP', 'AC'], 'CAPITAL': ['MANAUS', 'MACAPÁ', 'RIO BRANCO']} 

df = pd.DataFrame(dic1)

print(df)

print("=================================================================")
print("Leitura de Arquivos CSV")
dados = pd.read_csv('/home/darklinux/Downloads/dados-curso.csv')

shp = dados.shape

print(shp)