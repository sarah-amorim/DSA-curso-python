import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm 

# Existe alguma relação entre a área de imóveis (em metros quadrados) e o valor do aluguel em uma determinada cidade? Caso exista relação, como podemos mensurá-la?

# Carregar dados 
df = pd.read_csv('dataset.csv')
df.shepe
df.columns
df.head()
df.info()

# Análise exploratória - Resumo estatística 
df.isnull().sum() # Verifica se há valores ausentes 
df.describe()  # Resumo estatístico do dataset 
# Nesse dataset, a coluna 'codigo_bairro' não possui valores quantitativos, então não faz sentido calcular a média

df["valor_aluguel"].describe() # Resumo estatístico da variável alvo (com base na pergunta de negócio)

sns.histplot(data = df, x = 'valor_aluguel', kde = True) # Histograma da variável alvo

df.corr() # Correlação entre as variáveis

# Vamos analisar a relação entre a variável de entrada area_m2 e variável alvo valor_aluguel 
sns.scatterplot(data = df, x = "area_m2", y = "valor_aluguel") # Casas maiores -> alugueis altos
