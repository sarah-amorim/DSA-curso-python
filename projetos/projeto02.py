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

