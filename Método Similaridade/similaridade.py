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
# ========== Carregando e Padronizando os Dados ==========
# Copiando o dataframe em análise
df_tsp = df.copy()

# Padronizando o dataframe df_tsp
scaler_tsp = StandardScaler()
df_tsp_scaled = pd.DataFrame(
    scaler_tsp.fit_transform(df_tsp),
    columns=df.columns
)

# ================ Gerando a Matriz de Distâncias ================
# Distâncias entre variáveis (colunas)
distance_vector = pdist(df_tsp_scaled.T, metric='euclidean')

# Convertendo o vetor condensado de distâncias para matriz quadrada simétrica.
distance_square = squareform(distance_vector)

# ==================== Implementação do TSP ====================
# Função que ao receber uma matriz utiliza o Nearest Neighbor
# para retornar a permutação linear das variáveis
def tsp_solver(matrix):
    """
    Resolve o problema de ordenação utilizando
    a heurística do Vizinho Mais Próximo (Nearest Neighbor).

    Parâmetros:
        matrix : matriz de distâncias entre variáveis

    Retorna:
        path : permutação linear das variáveis
    """

    n = len(matrix)
    visited_nodes = [False] * n
    path = [0]
    visited_nodes[0] = True

    for _ in range(n - 1):
        current = path[-1]

        next_node = min(
            (j for j in range(n) if not visited_nodes[j]),
            key=lambda j: matrix[current][j]
        )

        path.append(next_node)
        visited_nodes[next_node] = True

    return path

# Obtendo a sequência ótima aproximada
tsp_sequence = tsp_solver(distance_square)

# ================= Reordenando a Matriz =================
# Calculando a Matriz de Correlação
correlation_matrix = df_tsp_scaled.corr()

# Aplicando a permutação obtida pelo TSP
tsp_matrix = correlation_matrix.iloc[tsp_sequence, :].iloc[:, tsp_sequence]

# =============== Visualizando a Matriz Reordenada ===============
# Gerando a Matriz Reordenada
heatmap_tsp = plot_heatmap(
    tsp_matrix,
    "Matriz Reordenada (TSP)"
)

# ================= Preparação dos Gráficos =================
# Renomeando a variável heatmap_original para original
original = heatmap_original

# Ajustando o títulos da Matriz Reordenada CH
clustering_hierarquico = heatmap_ch.properties(
    title={
        "text": "Matriz Reordenada",
        "subtitle": "Clustering Hierárquico"
    }

)

# Ajustando o títulos da Matriz Reordenada CH + OLO
clustering_olo = heatmap_ch_olo.properties(
    title={
        "text": "Matriz Reordenada",
        "subtitle": "Clustering Hierárquico + OLO"
    }

)

# Ajustando o títulos da Matriz Reordenada TSP
tsp = heatmap_tsp.properties(
    title={
        "text": "Matriz Reordenada",
        "subtitle": "Traveling Salesman Problem (TSP)"
    }

)

# ==================== Visualizando o Gráfico Final ====================
# Comparando a Matriz Original com as Matrizes Reordenadas no formato 2x2
# E configurando os títulos e os eixos de ambos os gráficos
heatmap_final = (
    (original | clustering_hierarquico) & (clustering_olo | tsp)
    ).configure_title(
        fontSize=20,
        lineHeight=22,
        anchor='middle'
    ).resolve_scale(
        color='shared'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14,
        titleFontWeight='bold'
    )

#heatmap_final

""" =================================== Conclusão =================================== """
"""
A comparação entre as quatro matrizes — Original, Reordenada por Clustering Hierárquico (CH), Reordenada por Clustering Hierárquico com Optimal Leaf Ordering (CH + OLO) e Traveling Salesman Problem (TSP) —
evidencia o impacto da reordenação na estrutura visual da matriz de correlação.

Na matriz original, observa-se uma dispersão das correlações ao longo da matriz, dificultando a identificação imediata de padrões estruturais.
Embora existam regiões de alta correlação, elas não estão organizadas, o que reduz a clareza visual da estrutura dos dados.

Com a aplicação do Clustering Hierárquico (CH), nota-se o surgimento de blocos mais concentrados próximos à diagonal principal.
Variáveis com comportamento semelhante passam a ser posicionadas em regiões adjacentes, revelando agrupamentos estruturais que não eram imediatamente visíveis na matriz original.
No entanto, a ordenação ainda apresenta pequenas descontinuidades internas aos grupos.

Ao aplicar o Clustering Hierárquico com Optimal Leaf Ordering (CH + OLO), observa-se uma organização melhor.
Os blocos de alta correlação tornam-se mais compactos e visualmente contínuos ao longo da diagonal, reduzindo a fragmentação observada no CH simples.
Essa melhoria ocorre porque o OLO otimiza a ordem das folhas do dendrograma, minimizando a distância entre elementos adjacentes e aproximando a matriz de uma estrutura Robinsoniana.

Já a reordenação via TSP também promove uma aproximação à estrutura diagonal, posicionando variáveis semelhantes de forma consecutiva.
Entretanto, diferentemente do CH + OLO, o TSP não preserva uma estrutura hierárquica explícita.
O resultado apresenta continuidade local forte entre elementos consecutivos, mas pode gerar transições menos estruturadas entre blocos maiores.

De modo geral, estes métodos de reordenação baseados em similaridade melhoram significativamente a legibilidade estrutural da matriz quando comparados à ordem original.
Além disso, embora baseados em princípios distintos, as três técnicas de reordenação baseada em similaridade analisadas produzem matrizes com organização próxima à estrutura Robinsoniana, evidenciada pela concentração de valores elevados ao longo da diagonal principal.

Assim, a análise comparativa confirma que a escolha do método de reordenação influencia diretamente a clareza visual da estrutura de correlação, sendo que, dentre os métodos analisados, o Clustering Hierárquico com OLO foi o que apresentou melhor desempenho visual no conjunto de dados analisado, com blocos mais definidos e continuidade mais evidente ao longo da diagonal, aproximando-se mais claramente do comportamento esperado de uma matriz aproximadamente Robinsoniana.
