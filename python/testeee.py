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



import pandas as pd
import os

def gerar_relatorio_funcionario_destaque(caminho_pasta, caminho_saida):
    # Listar os arquivos Excel na pasta
    arquivos_excel = [arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.endswith(".xlsx")]

    if not arquivos_excel:
        print("Nenhuma planilha encontrada no diretório.")
        return

    # Carregar as planilhas em DataFrames
    planilhas = [pd.read_excel(os.path.join(caminho_pasta, arquivo)) for arquivo in arquivos_excel]

    # Consolidar as planilhas em um único DataFrame
    df_consolidado = pd.concat(planilhas, ignore_index=True)

    # Analisar o desempenho dos funcionários (total de vendas por vendedor e esteira)
    desempenho_por_funcionario = (
        df_consolidado.groupby(['usuario_id', 'vendedor', 'esteira'])
        .size()
        .reset_index(name='total_vendas')
    )

    # Ordenar pelo maior número de vendas
    desempenho_por_funcionario = desempenho_por_funcionario.sort_values(by='total_vendas', ascending=False)

    # Garantir que o diretório de saída existe
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

    # Salvar o relatório em Excel
    desempenho_por_funcionario.to_excel(caminho_saida, index=False)

    print(f"Relatório gerado com sucesso: {caminho_saida}")

if __name__ == "__main__":
    # Caminho da pasta contendo as planilhas
    caminho_pasta = r"C:\\Users\\06010940184\\teste\\APENAS TESTE"

    # Caminho completo do arquivo de saída
    caminho_saida = r"C:\\Users\\06010940184\\teste\\APENAS TESTE\\relatorio_funcionario_destaque.xlsx"

    # Gerar o relatório
    gerar_relatorio_funcionario_destaque(caminho_pasta, caminho_saida)













"""maiorVenda = 0
while contador <= 3:
    for valores in vendedorLoja["Valor"]:
        if valores > maiorVenda:
            maiorVenda = valores
            contador +=1
            print(maiorVenda)







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
"""