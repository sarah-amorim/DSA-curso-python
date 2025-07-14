import numpy as np # Manipulação de dados 
import pandas as pd # Para usar a linguagem SQL com a sintaxe do Pandas 
import matplotlib.pyplot as plt # Gráficos 
import seaborn as snd # Gráficos 
import datetime as dt # Manipulação de data 

df = pd.read_csv('dataset/dataset.csv') # Carrega o dataset 
df.shape # Shape (linhas, colunas)
df.head() # Amostra das 5 primeiras linhas 
df.tail() # Amostra das 5 últimas linhas 

# Análise Exploratória 

df.columns # Colunas do conjunto de dados 
df.dtypes # Verifica o tipo de dado de cada coluna 
df['Valor_Venda'].describe() # Resumo estatístico da coluna com valor de venda (quantitativo)
df[df.duplicated()] # Retorna verdadeiro para cada linha que tiver valor duplicado
# Se houver registros duplicados, isso precisa ser resolvido!
df.isnull().sum() # Total de valores nulos para cada coluna 
# Valores ausentes são um problema! 

# Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

# Filtramos o dataframe com os registros da categoria que desejamos
df1 = df[df['Categoria'] == 'Office Suplies']
# Agrupamos por cidade e calculamos o total de valor_vendas
df1_cidade_valor = df1.groupby('Cidade')['Valor_Venda'].sum()
# Encontramos a cidade com maior número de vendas 
cidade_maior_venda = df1_cidade_valor.idxmax()
# Para conferir o resultado 
df1_cidade_valor.sort_values(ascending=False) 

# Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.
df2 = df('Data_Pedido')['Valor_Venda'].sum()
df2.head()
# Plot 
plt.figure(figsize= (20,6))
df2.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green')
plt.title('Total de Vendas Por Data Pedido')
plt.show()

# Qual Total de Vendas por Estado? Demonstre o resultado através de um gráfico de barras.
df3 = df('Estado')['Valor_Venda'].sum().reset_index()
plt.figure(figsize=(16,6))
sns.barplot(data = df3, y = 'Valor_Venda', x = 'Estado').set(title='Vendas Por Estado')
plt.xticks(rotation = 80)
plt.show()

# Quais São as 10 Cidades Com Maior Total de Vendas? Demonstre o resultado atráves de um gráfico de barras.
df4 = df.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending=False).head(10)
plt.figure(figsize=(16,6))
snd.barplot(data=df4, x = 'Cidade', y='Valor_Venda').set(title='As 10 cidades com maior total de vendas')
plt.show()

# Qual Segmento Tem o Maior Total de Vendas? Demonstre o resultado atráves de  um gráfico  de pizza
pd.options.display.float_format = '{:,.4f}'.format # print with default float settings
df5 = df.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending=False)
