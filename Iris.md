🌸 Estrutura do dataset Iris
Cada linha representa uma flor, e as colunas são:
📊 Campos (colunas)
1. sepal length (comprimento da sépala)

Medido em centímetros
Representa o tamanho da sépala (parte externa da flor)


2. sepal width (largura da sépala)

Também em centímetros
Mede a largura da sépala


3. petal length (comprimento da pétala)

Em centímetros
Uma das medidas mais importantes para diferenciar espécies


4. petal width (largura da pétala)

Em centímetros
Muito útil para classificação


5. species (espécie)

É a classe (target) do dataset
Valores possíveis:

Iris-setosa
Iris-versicolor
Iris-virginica




🧠 Interpretação geral

As 4 primeiras colunas → variáveis numéricas (features)
A última coluna → variável categórica (rótulo)


📌 Exemplo de linha
5.1, 3.5, 1.4, 0.2, Iris-setosa

👉 Significa:

Sépala: 5.1 cm (comprimento), 3.5 cm (largura)
Pétala: 1.4 cm (comprimento), 0.2 cm (largura)
Espécie: Setosa


🎯 Para que serve
Esse dataset é usado principalmente para:

Classificação supervisionada
Testar algoritmos como:

KNN
SVM
Árvores de decisão




✅ Resumo
👉 O iris.data.csv contém:

4 medidas físicas da flor
1 rótulo indicando a espécie

👉 Objetivo comum:
Prever a espécie da flor com base nas medidas