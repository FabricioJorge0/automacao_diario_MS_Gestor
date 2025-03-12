#importar a base de dados;
import pandas as pd
import heapq

tabela_vendas = pd.read_excel("DIARIO INPUT V.37.xlsb", sheet_name="Esteira", header=1)

contador = 0

# visualizar a base de dados;
pd.set_option("display.max_columns", None)
# faturamento por vendedor
vendedorLoja = tabela_vendas[["vendedor", "Valor"]].groupby("vendedor").sum()
print(heapq.nlargest(3, vendedorLoja["Valor"]))


#pip install pyxlsb    --- instalar isso aqui aaaaaaaa


print("-"*50)

"""maiorVenda = 0
while contador <= 3:
    for valores in vendedorLoja["Valor"]:
        if valores > maiorVenda:
            maiorVenda = valores
            contador +=1
            print(maiorVenda)"""




""".groupby("vendedor").sum()
print(vendedor)

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
enviar email com relátório;"""