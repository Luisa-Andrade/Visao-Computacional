# Visão Computacional

| Grupo         |
|---------------|
| João Victor Lima    |
| Luisa de Andrade |
| Thiago Moraes |

## EPs 1
- A pasta banco-de-imagens contém as imagens dos objetos que foram solicitadas, nomeadas da seguinte forma: <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Nome do objeto e a variação do mesmo - variação entre dia e noite - variação dentro ou fora (in/out) - variação do fundo .csv <br>
- A Tabela-Detalhada contém a tabela com todas informações por imagem da seguinte forma: <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Nome do objeto | Variação do Objeto | Dia/Noite | Ambiente | Fundo | Tamanho (KB) | Dimensão (pixels) (Largura x Altura) | URL da Imagem <br>
- A Tabela-Global contém a tabela com as seguintes informações: <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Número de Classes	| Número de Imagens | Tamanho da Base (bytes) <br>
- O EPs-1 contém o código em Python que visualiza a base usando funções MNIST-like. <br>
<br>

## EPs 2.1
- A pasta originalGrayDataSet contém as imagens em níveis de cinza. <br>
- A pasta augmentedDataSet contém as imagens com as seguintes funções: <br>
&nbsp;&nbsp;&nbsp;&nbsp;- RGB2gray; <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Soma de fundo com gradiente de níveis de cinza; <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Logaritmo da imagem; <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Exponencial da imagem; <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Filtro da média implementado usando convolução. <br>
- A Tabela-Detalhada-EP2.1 contém a tabela com todas as informações das imagens originais junto com o augmentedDataSet. Da seguinte forma: <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Nome do objeto | Variação do Objeto | Dia/Noite | Funções | Ambiente | Fundo | Tamanho (KB) | Dimensão (pixels) (Largura x Altura) | URL da Imagem <br>
- O EP2.1 contém o código em Python que visualiza a base usando funções MNIST-like.

#EPs 2.2
- A pasta normalizedDataSet contém as imagens com as seguinter funções: <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Protótipo médio de cada classe; <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Histograma médio de cada classe; <br>
&nbsp;&nbsp;&nbsp;&nbsp;- Variância do histograma de cada classe. <br>
- A pasta Códigos-Utilizados contém os códigos necessários para o EPs 2.1 e o EPs 2.2.
