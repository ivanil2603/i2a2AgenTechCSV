import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from langchain.tools import tool

@tool
def plotar_histogramas_gerais(df: pd.DataFrame) -> plt.Figure:
    """
    Útil para visualizar a distribuição de TODAS as variáveis numéricas do dataframe.
    Use esta ferramenta quando o usuário pedir 'os histogramas', 'distribuição das variáveis' ou algo similar em um sentido geral.
    Cria uma grade de histogramas, um para cada coluna numérica.
    Retorna um único objeto de figura do Matplotlib contendo todos os subplots.
    """
    df_numerico = df.select_dtypes(include=['number'])
    if df_numerico.empty:
        raise ValueError("O dataframe não contém colunas numéricas para plotar.")

    num_cols = len(df_numerico.columns)
    # Calcula um layout de grade razoável para os subplots
    n_grid_cols = math.ceil(math.sqrt(num_cols))
    n_grid_rows = math.ceil(num_cols / n_grid_cols)

    fig, axes = plt.subplots(n_grid_rows, n_grid_cols, figsize=(n_grid_cols * 5, n_grid_rows * 4))
    axes = axes.flatten()  # Transforma a grade 2D de eixos em uma lista 1D

    for i, col in enumerate(df_numerico.columns):
        sns.histplot(df_numerico[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribuição de {col}')

    # Oculta eixos não utilizados se o número de plots for menor que a grade
    for i in range(num_cols, len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    return fig