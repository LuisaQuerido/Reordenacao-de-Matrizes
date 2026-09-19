# Abordagem Robinsoniana

Para representar esse método, escolhemos implementar a **abordagem Robinsoniana** utilizando três técnicas de reordenação:

1. **Clustering Hierárquico**
2. **Clustering Hierárquico + Optimal Leaf Ordering (OLO)**
3. **Traveling Salesman Problem (TSP)**

No artigo *Matrix Reordering Methods for Table and Network Visualization*, os autores classificam a abordagem Robinsoniana (*Robinsonian approaches*) como os métodos que constroem uma matriz de similaridade e buscam aplicar uma permutação que aproxime essa matriz a uma **matriz de Robinson**.

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

### I. Distância Euclidiana — \( L_{2} \)

A distância Euclidiana é um caso particular da distância de Minkowski para \(p=2\):

$$

d_E(x,y)
=
\left(
\sum_{i=1}^{p}
|x_i-y_i|^2
\right)^{1/2}

$$

$$

d_E(x,y)
=
\sqrt{
\sum_{i=1}^{p}
(x_i-y_i)^2
}

$$


### II. Distância Euclidiana ao quadrado — \(L_{2}^2\)

A distância Euclidiana ao quadrado é definida por:

$$

d_{E^2}(x,y)
=
\sum_{i=1}^{p}
(x_i-y_i)^2

$$

### III. Distância de Manhattan — \(L_{1}\)

A distância de Manhattan, também conhecida como distância \(L_{1}\), é dada por:

$$

d_M(x,y)
=
\sum_{i=1}^{p}
|x_i-y_i|

$$

### IV. Distância de Chebyshev — \(L_{\infty\})

A distância de Chebyshev corresponde ao maior valor absoluto da diferença entre os atributos:

$$
d_C(x,y)
=
\max_{1 \leq i \leq p}
|x_i-y_i|
$$

## Métrica utilizada

Para a análise das diferentes técnicas de reordenação, utilizaremos a **Distância Euclidiana (\(L_{2}\))** como medida de distância entre as observações.
