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
