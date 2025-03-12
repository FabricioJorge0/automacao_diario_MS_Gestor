#importanção de biblioteca;
import pandas as pd

#importar a base de dados;
tabela_vendas = pd.read_excel("DIARIO INPUT V.37.xlsb", sheet_name="Esteira", header=1)

# configurando melhor visualização geral da base de dados;
pd.set_option("display.max_columns", None)

# Filtrando colunas da planilha, somando os valores e capturando as 3 maiores
vendedorLoja = tabela_vendas[["vendedor", "Valor"]].groupby("vendedor").sum().nlargest(3, "Valor")
print(vendedorLoja)


#pip install pyxlsb    --- instalar isso aqui aaaaaaaa

print("-"*50)


