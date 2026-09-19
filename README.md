# Reordenação de Matrizes

## por Luísa Querido e Sofia Guaranho

### Tópicos
- Visão Geral da Reordenação
- Objetivos da Reordenação
- Alguns Métodos
- Por que reordenar matrizes?
- Conjunto de Dados e de Bibliotecas
- Estratégias e Implementações dos Métodos
- Conclusão
- Bibliografia

_______________________________________
#### Visão Geral da Reordenação

*Reordenação de matrizes* é o processo de permutar linhas e colunas de uma matriz com o objetivo de revelar estruturas ocultas, padrões, agrupamentos ou regularidades nos dados.

Geralmente, a ordem original de uma matriz não carrega significado estrutural. Em muitos casos, a disposição das linhas e colunas é arbitrária.

A matriz que é gerada pela reordenação contém os mesmos dados da matriz original, mas apresenta eles com uma ordem diferente, o que pode tornar padrões visuais significativamente mais evidentes.

A reordenação não é apenas um problema algorítmico, mas também um processo exploratório. Os usuários podem interagir, arrastar, reorganizar e testar diferentes ordens para descobrir padrões.

Essa reordenação pode revelar:

* Agrupamentos
* Bandas
* Estruturas de Grafo
* Estruturas em Blocos
* Estruturas Hierárquicas
* Padrões Diagonais

_______________________________________
#### Objetivos da Reordenação

A *Análise sobre a Reordenação de Matrizes* tem como objetivo: agrupar os elementos semelhantes próximos uns dos outros (*Agrupamento/Clustering*); organizar a matriz para formar blocos densos ao longo da diagonal (*Estruturas em Blocos/Block Structure*); minimizar a distância entre elementos não nulos e a diagonal principal (*Redução de Largura de Banda/Bandwidth reduction*); e encontrar uma ordem linear que preserve similaridade.

Este *notebook* pretende apresentar diferentes métodos de reordenação de matrizes. A linguagem escolhida foi o *Python* do *Google Colab* e suas bibliotecas: ```Numpy```, ```Pandas```, ```Altair```, ```Seaborn```, ```Matplotlib```, ```Scikit-learn``` e ```Python_tsp```.

A seguir usaremos uma base de dados, disponível em: [https://www.kaggle.com/datasets/yasserh/wine-quality-dataset/data](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset/data), para visualizar os métodos propostos.

_______________________________________
#### Alguns métodos

* **Métodos Baseados em Similaridade:** Reordenam linhas e colunas com base em medidas de similaridade entre vetores. Exemplo: Distância Euclidiana, Correlação e Similaridade de Jaccard. Geralmente combinados com: Hierarchical Clustering (Agrupamento Hierárquico);

* **Métodos Espectrais:** Utilizam autovalores e autovetores da matriz ou do grafo associado para determinar uma ordem ótima. Baseiam-se na decomposição espectral: Laplaciano do grafo e Fiedler vector. Muito importante para fundamentação matemática;

_______________________________________
#### Por que reordenar matrizes?

A reorganização de matrizes agrupa dados semelhantes para revelar correlações e agrupamentos (clusters) que seriam invisíveis em tabelas desordenadas. Para Jacques Bertin, a matriz deve ser móvel para funcionar como um processador visual, pois a ordenação permite que a percepção humana identifique blocos homogêneos instantaneamente. Processar uma matriz ordenada é significativamente mais fácil e eficiente, pois substitui a leitura individual de cada célula por uma visão de conjunto que reduz a carga cognitiva e torna a análise imediata.
