# Abordagem Robinsoniana

Para representar esse método, escolhemos implementar a **abordagem Robinsoniana** utilizando três técnicas de reordenação:

1. **Clustering Hierárquico**
2. **Clustering Hierárquico + Optimal Leaf Ordering (OLO)**
3. **Traveling Salesman Problem (TSP)**

No artigo Matrix Reordering Methods for Table and Network Visualization, os autores descrevem que algumas abordagens de reordenação modelam o problema como uma otimização combinatória, buscando uma permutação linear que minimize a soma das distâncias entre elementos consecutivos.

Formalmente, seja $π ∈ S_n$ uma permutação das variáveis, o problema pode ser formulado como:

$$
\min_{π ∈ S_n}{\sum_{i=1}^{n-1} d(π_i, π_{i+1})}
$$

onde:

*   cada variável é modelada como um vértice;
*   $d(⋅,⋅)$ representa uma métrica de distância;
*   a solução $π$ define uma ordenação linear das variáveis.

Diferentemente do TSP clássico, não consideramos o fechamento do ciclo, pois o objetivo é obter uma sequência linear e não um percurso circular.

Utilizamos a heurística do vizinho mais próximo *(Nearest Neighbor)* para obter uma solução aproximada do *Traveling Salesman Problem (TSP)*.

Embora existam algoritmos exatos para o TSP, o problema é NP-difícil e sua complexidade cresce exponencialmente com o número de variáveis, tornando a solução ótima impraticável para matrizes de tamanho moderado.

Conforme discutido no artigo supracitado, abordagens heurísticas são amplamente utilizadas no contexto de reordenação de matrizes por serem computacionalmente eficientes e adequadas para análise visual exploratória.

Ao minimizar a soma das distâncias entre elementos adjacentes, o método tende a posicionar variáveis mais similares próximas na ordenação final, favorecendo uma estrutura aproximadamente Robinsoniana.

No artigo *Matrix Reordering Methods for Table and Network Visualization*, os autores também classificam a abordagem Robinsoniana (*Robinsonian approaches*) como os métodos que constroem uma matriz de similaridade e buscam aplicar uma permutação que aproxime essa matriz a uma **matriz de Robinson**.

## Matriz de Robinson

> **Definição: Matriz de Robinson**
>
> Uma matriz simétrica \(R\) é chamada de **matriz de similaridade de Robinson** se seus valores decrescem monotonicamente ao se afastar da diagonal principal.
>
> Formalmente, para índices \(i < j < k\):
>
> $$
> R_{i,k} \leq R_{i,j}
> $$
>
> De forma equivalente, a similaridade diminui quanto mais distante da diagonal principal.
>
> No caso de uma **matriz de distâncias**, a propriedade é invertida: os valores aumentam monotonicamente ao se afastar da diagonal.

## Métricas de distância

Algumas medidas de distância entre um par de observações \(x\) e \(y\), com \(p\) atributos, derivam da **função de Minkowski**, dada por:

$$
d(x,y) =
\left(
\sum_{i=1}^{p}
|x_i-y_i|^p
\right)^{1/p}
$$

Algumas dessas métricas serão formuladas a seguir.

### I. Distância Euclidiana — $L_2$

A distância Euclidiana é um caso particular da distância de Minkowski para \(p=2\):

$$
d_E(x,y) =
\sqrt{
\sum_{i=1}^{p}
(x_i-y_i)^2
}
$$

### II. Distância Euclidiana ao quadrado — $L_2^2$

A distância Euclidiana ao quadrado é definida por:

$$
d_{E^2}(x,y) =
\sum_{i=1}^{p}
(x_i-y_i)^2
$$

### III. Distância de Manhattan — $L_1$

A distância de Manhattan, também conhecida como distância $L_1$, é dada por:

$$
d_M(x,y) =
\sum_{i=1}^{p}
|x_i-y_i|
$$

### IV. Distância de Chebyshev — $L_\infty$

A distância de Chebyshev corresponde ao maior valor absoluto da diferença entre os atributos:

$$
d_C(x,y) =
\max_{1 \leq i \leq p}
|x_i-y_i|
$$

## Métrica utilizada

Para a análise das diferentes técnicas de reordenação, utilizaremos a **Distância Euclidiana ($L_2$)** como medida de distância entre as observações.
