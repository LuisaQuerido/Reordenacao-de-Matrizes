# Importações
import numpy as np                                    # Operações numéricas e matrizes
import pandas as pd                                   # Manipulação de dados
import altair as alt                                  # Visualização interativa
from sklearn.datasets import load_wine                # Dataset Wine
from scipy.spatial.distance import pdist              # Distância entre pontos
from sklearn.preprocessing import StandardScaler      # Padronização dos dados
from scipy.cluster.hierarchy import linkage, optimal_leaf_ordering, leaves_list

# Configurações do Altair
alt.renderers.enable('default')                       # Habilita a renderização padrão
alt.data_transformers.disable_max_rows()              # Remove o limite de linhas

# Carregando os dados
wine = load_wine()

# Transformando em Dataframe
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df.head()

""" ==== Função que faz o heatmap dependendo da matriz e do título do gráfico ==== """
def plot_heatmap(matriz, title):
    """
    Convertendo matriz para formato longo para gerar o heatmap no Altair
    """

    ordem = list(matriz.columns)

    matriz_long = (
        matriz
        .reset_index()
        .melt(id_vars='index')
        .rename(columns={
            'index': 'Variável no Eixo X',
            'variable': 'Variável no Eixo Y',
            'value': 'Correlação'
        })
    )

    heatmap = alt.Chart(matriz_long).mark_rect().encode(
        x=alt.X('Variável no Eixo X:O', sort=ordem, title='Variáveis'),
        y=alt.Y('Variável no Eixo Y:O', sort=ordem, title='Variáveis'),
        color=alt.Color('Correlação:Q',
                        scale=alt.Scale(scheme='purples'),
                        title='Correlação'),
        tooltip=['Variável no Eixo X', 'Variável no Eixo Y', 'Correlação']
    ).properties(
        width=300,
        height=300,
        title=title
    )

    return heatmap

# Observação:

# Foi necessário especificar explicitamente a ordenação das categorias nos eixos do Altair
# com a lista ordem, pois a biblioteca aplica ordenação automática para variáveis ordinais,
# o que pode ocultar a permutação produzida pelo algoritmo de reordenação.

""" ==================== Matriz Original ==================== """
# ========== Carregando e Padronizando os Dados ==========
# Copiando o dataframe em análise
df_original = df.copy()

# Padronizando o dataframe df_original
scaler_tsp = StandardScaler()
df_original_scaled = pd.DataFrame(
    scaler_tsp.fit_transform(df_original),
    columns=df.columns
)

# ========== Gerando a Matriz de Similaridade ==========
# Gerando uma Matriz de Similaridade do tipo Matriz de Correlação
original_corr = df_original_scaled.corr()

# ========== Visualizando a Matriz Original ==========
# Gerando um heatmap para a Matriz corr e o título "Matriz de Correlação Original"
heatmap_original = plot_heatmap(original_corr, "Matriz de Correlação Original")


""" ===================== Clustering Hierárquico ===================== """
# ========== Carregando e Padronizando os Dados ==========
# Copiando o dataframe em análise
df_ch = df.copy()

# Padronizando o dataframe df_original
scaler_ch = StandardScaler()
df_ch_scaled = pd.DataFrame(
    scaler_ch.fit_transform(df_ch),
    columns=df_ch.columns
)

# ================ Gerando a Matriz de Similaridade ================
# Gerando uma Matriz de Similaridade do tipo Matriz de Correlação
matriz_sim_hc = df_ch_scaled.corr()

# ===== Convertendo a Similaridade em Distância e Condensando a Matriz =====
# Construindo uma Matriz de Distância Condensada com a Distância Euclidiana
dist_ch = pdist(df_ch_scaled.T, metric='euclidean')

# ====== Aplicando o Clutering Hierárquico e o Optimal Leaf Ordering ======
# Aplicando o Clustering Hierárquico com average linkage
Z_ch = linkage(dist_ch, method='average')

# ========== Reordenando as variáveis e a Matriz ==========
# Obtendo a reordenação das variáveis
ordem_ch = leaves_list(Z_ch)

# Reordenando a Matriz
matriz_reordenada_ch = matriz_sim_hc.iloc[ordem_ch, :].iloc[:, ordem_ch]

# =============== Visualizando a Matriz Reordenada ===============
# Gerando a Matriz Reordenada
heatmap_ch = plot_heatmap(
    matriz_reordenada_ch,
    "Matriz Reordenada (Clustering Hierárquico)"
)

""" ======== Clustering Hierárquico + Optimal Leaf Ordering (OLO) ======== """
# ========== Carregando e Padronizando os Dados ==========
# Copiando o dataframe em análise
df_ch_olo = df.copy()

# Padronizando o dataframe df_ch_olo
scaler_ch_olo = StandardScaler()
df_ch_olo_scaled = pd.DataFrame(
    scaler_ch_olo.fit_transform(df_ch_olo),
    columns=df.columns
)

# ========== Gerando a Matriz de Similaridade ==========
# Gerando uma Matriz de Similaridade do tipo Matriz de Correlação
ch_olo_corr = df_ch_olo_scaled.corr()

# ===== Convertendo a Similaridade em Distância e Condensando a Matriz =====
# Construindo uma Matriz de Distância Condensada com a Distância Euclidiana
condensed_ch_olo = pdist(df_ch_olo_scaled.T, metric='euclidean')

# ====== Aplicando o Clutering Hierárquico e o Optimal Leaf Ordering ======
# Aplicando o Clustering Hierárquico com average linkage
Z = linkage(condensed_ch_olo, method='average')

# Aplicando o Optimal Leaf Ordering (OLO)
Z_opt = optimal_leaf_ordering(Z, condensed_ch_olo)

# ========== Reordenando as variáveis e a Matriz ==========
# Obtendo a reordenação das variáveis
order = leaves_list(Z_opt)

# Reordenando a Matriz
reordered_ch_olo_corr = ch_olo_corr.iloc[order, :].iloc[:, order]

# =============== Visualizando a Matriz Reordenada ===============
# Gerando a Matriz Reordenada
heatmap_ch_olo = plot_heatmap(
    reordered_ch_olo_corr,
    "Matriz Reordenada (Clustering Hierárquico + OLO)"
)

""" ===================== Traveling Salesman Problem (TSP) ===================== """
