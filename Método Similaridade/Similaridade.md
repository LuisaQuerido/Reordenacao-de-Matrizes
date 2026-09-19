Para representar esse método, escolhemos implementar a abordagem Robinsoniana utilizando três técnicas de reordenação:
1. *Clustering Hierárquico*

2. *Clustering Hierárquico* $ $ $+$ *Optimal Leaf Ordering (OLO)*

3. *Traveling Salesman Problem (TSP)*

No artigo Matrix Reordering Methods for Table and Network Visualization, os autores classificam a abordagem Robinsoniana (*Robinsonian approaches*) como os métodos que constroem uma matriz de similaridade e buscam aplicar uma permutação que aproxime essa matriz a uma matriz de Robinson.

> **Definição: Matriz de Robinson**
>
> Uma matriz simétrica $R$ é chamada de matriz de similaridade de Robinson se seus valores decrescem monotonicamente ao se afastar da diagonal principal.
>
> Formalmente, para índices $i < j < k$:
>
> <center> $R_{i,k} ≤ R_{i,j}$ </center>
>
> E de forma equivalente, a similaridade diminui quanto mais distante da diagonal.
>
> No caso de matriz de distâncias, a propriedade é invertida: os valores aumentam monotonicamente ao se afastar da diagonal.

Algumas medidas de distância entre um par de observações $ d(x,y) $ derivam da função de Minkowsky, dada por:
<center> $$ d(x,y) = (\sum_{i=1}^{p}|x_i - y_i|^p)^{1/p} $$</center>

Algumas dessas métricas serão formuladas a seguir:
<ol type="I">
  <li> Distância Euclidiana - $L_2$
$$ d_{E}(x,y) = (\sum_{i=1}^{2}|x_i - y_i|^2)^{1/2} = \sqrt{\sum_{i=1}^{2}(x_i - y_i)^2} $$ </li>

  <li> Distância Euclidiana²
$$ d_{E^2}(x,y) = \sum_{i=1}^{2}(x_i - y_i)^2 $$ </li>

  <li> Distância de Manhattan - $L_1$
$$ d_{M}(x,y) = \sum_{i=1}^{1}|x_i - y_i| $$ </li>

  <li> Distância de Chebyshev - $L_{\infty}$
$$ d_{C}(x,y) = \max|x_i - y_i|$$ </li>

</ol>

Para a análise das diferentes técnicas utilizaremos a métrica da Distância Euclidiana - $L_2$.
