import pandas as pd
import os

def gerar_relatorio_funcionarios_destaque(pasta_entrada, pasta_saida):
    # Localizar o arquivo .xlsb na pasta de entrada
    arquivo_xlsb = None
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.endswith(".xlsb"):
            arquivo_xlsb = os.path.join(pasta_entrada, arquivo)
            break

    if not arquivo_xlsb:
        print("Erro: Nenhum arquivo .xlsb encontrado na pasta de entrada.")
        return

    print(f"Arquivo encontrado: {arquivo_xlsb}")

    # Carregar as abas necessárias
    abas_foco = ['Esteira', 'Usuarios', 'Datas', 'METAS']
    dados_planilha = {aba: pd.read_excel(arquivo_xlsb, sheet_name=aba, engine='pyxlsb') for aba in abas_foco}

    # Ajustar os cabeçalhos da aba "Esteira"
    dados_planilha["Esteira"].columns = dados_planilha["Esteira"].iloc[0]
    dados_planilha["Esteira"] = dados_planilha["Esteira"].drop(0).reset_index(drop=True)

    # Normalizar nomes de colunas
    for aba in dados_planilha:
        dados_planilha[aba].columns = dados_planilha[aba].columns.str.strip().str.lower()

    # Converter a coluna "data_movimentacao" para data
    dados_planilha["Esteira"]["data_movimentacao"] = pd.to_numeric(dados_planilha["Esteira"].get("data_movimentacao"), errors="coerce")
    dados_planilha["Esteira"]["data_movimentacao"] = pd.to_datetime(dados_planilha["Esteira"]["data_movimentacao"], origin="1899-12-30", unit="D")

    # Filtrar vendas do mês atual
    mes_atual = pd.Timestamp.now().month
    ano_atual = pd.Timestamp.now().year
    vendas_mes_atual = dados_planilha["Esteira"][
        (dados_planilha["Esteira"]["data_movimentacao"].dt.month == mes_atual) &
        (dados_planilha["Esteira"]["data_movimentacao"].dt.year == ano_atual)
    ]

    # Analisar desempenho por funcionário
    desempenho_mes = (
        vendas_mes_atual.groupby(["usuario_id", "vendedor", "esteira"])
        .size()
        .reset_index(name="total_vendas")
        .sort_values(by="total_vendas", ascending=False)
    )

    # Mapear supervisores
    mapa_supervisores = vendas_mes_atual.groupby("usuario_id")["supervisor"].agg(pd.Series.mode)
    mapa_supervisores = mapa_supervisores.map(lambda x: x[0] if isinstance(x, pd.Series) else x)
    desempenho_mes["supervisor"] = desempenho_mes["usuario_id"].map(mapa_supervisores)

    # Unir metas com desempenho
    desempenho_com_metas = desempenho_mes.merge(
        dados_planilha["metas"],
        left_on="supervisor",
        right_on="superiorimediato",
        how="left"
    )

    # Calcular a relação entre o total de vendas e as metas
    colunas_metas = [
        "altas_móveis*", "pn_móvel*", "banda_larga*", "receita_de_altas*",
        "renovação_móvel_(fisíco)*", "renovação_ftth_(físico)*", "energia*",
        "renovação_total", "renovação_+_pp"
    ]

    for coluna in colunas_metas:
        nome_novo = f"%_meta_{coluna.replace('*', '').replace(' ', '_')}"
        desempenho_com_metas[nome_novo] = (desempenho_com_metas["total_vendas"] / desempenho_com_metas[coluna]) * 100

    desempenho_com_metas.replace([float('inf'), float('nan')], 0, inplace=True)

    # Selecionar colunas relevantes para o relatório
    colunas_relatorio = [
        "usuario_id", "vendedor", "supervisor", "esteira", "total_vendas"
    ] + [f"%_meta_{coluna.replace('*', '').replace(' ', '_')}" for coluna in colunas_metas]

    relatorio_destaques = desempenho_com_metas[colunas_relatorio]

    # Garantir que a pasta de saída exista
    os.makedirs(pasta_saida, exist_ok=True)

    # Caminho de saída do relatório
    caminho_saida = os.path.join(pasta_saida, "relatorio_funcionarios_destaque.xlsx")

    # Salvar o relatório em Excel
    relatorio_destaques.to_excel(caminho_saida, index=False)
    print(f"Relatório gerado com sucesso: {caminho_saida}")

if __name__ == "__main__":
    pasta_entrada = r"C:\\Users\\06010940184\\teste"
    pasta_saida = r"C:\\Users\\06010940184\\teste\\APENAS TESTE\\saida"
    gerar_relatorio_funcionarios_destaque(pasta_entrada, pasta_saida)