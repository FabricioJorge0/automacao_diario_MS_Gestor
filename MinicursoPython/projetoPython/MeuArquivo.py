#importar a base de dados;
import pandas as pd
tabela_vendas = pd.read_excel("Vendas.xlsx")

# visualizar a base de dados;
pd.set_option("display.max_columns", None)

# faturamento por loja;
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento)

print("-"*50)
# quantidade de produtos vendidos por loja;
quantidade_loja = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade_loja)

print("-"*50)
# ticket médio por produto em cada loja;
ticket_medio = (faturamento["Valor Final"] / quantidade_loja["Quantidade"]).to_frame()
print(ticket_medio)

#for valorFaturamento in faturamento[["ID Loja", "Valor Final"]]:
 #   for valorQuantidade in quantidade_loja[["ID Loja", "Quantidade"]]:
  #      resultado = valorFaturamento["Valor Final"] /valorQuantidade["Quantidade"]
   #     print(resultado)
# enviar email com relátório;