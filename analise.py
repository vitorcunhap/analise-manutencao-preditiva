import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df= pd.read_csv('predictive_maintenance.csv')

# Primeiras informações 
print(df.head())
print('\nFormato do dataset:', df.shape)
print('\nColunas:', df.columns.tolist())

# Quantas falhas existem?
print('\nDistribuição de falhas:')
print(df['Failure Type'].value_counts())

# Gráfico de tipos de falha
plt.figure(figsize=(10,5))
df['Failure Type'].value_counts().plot(kind='bar',color='steelblue')
plt.title('Distribuição de Tipos de Falha')
plt.xlabel('Tipo de Falha')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('falhas.png')
plt.show()

# Relação entre temperatura do ar e falhas
plt.figure(figsize=(10, 5))
sns.boxplot(x='Failure Type', y='Air temperature [K]', data=df)
plt.title('Temperatura do Ar por Tipo de Falha')
plt.xlabel('Tipo de Falha')
plt.ylabel('Temperatura do Ar [K]')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperatura_falhas.png')
plt.show()

# Desgaste da ferramenta por tipo de falha
plt.figure(figsize=(10, 5))
sns.boxplot(x='Failure Type', y='Tool wear [min]', data=df)
plt.title('Desgaste da Ferramenta por Tipo de Falha')
plt.xlabel('Tipo de Falha')
plt.ylabel('Desgaste [min]')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('desgaste_falhas.png')
plt.show()