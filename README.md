# Desafio de Ciência de Dados - Recomendação de Filmes para PProductions

Este repositório contém a resolução do Desafio de Ciência de Dados proposto pela Indicium. O objetivo é analisar uma base de dados cinematográfica para orientar o estúdio de Hollywood PProductions sobre qual tipo de filme desenvolver.

O projeto abrange uma Análise Exploratória dos Dados (EDA), a construção de um modelo de Machine Learning para prever a nota do IMDB, e as respostas às questões de negócio propostas.

## Estrutura do Repositório
* /
* ├── content/
* │   └── desafio_indicium_imdb.csv   / Dados utilizados na análise
* ├── desafio-lighthouse.ipynb        / Notebook com a EDA e o desenvolvimento do modelo
* ├── main.pkl                        / Modelo de previsão treinado e salvo
* ├── main.py                         / Script para interagir com o modelo
* ├── requirements.txt                / Lista de dependências do projeto
* └── README.md                       / Este arquivo
  
## Como Instalar e Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior
* Pip (gerenciador de pacotes do Python)

### Passos para Execução

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/brunoaudricc/LH_CD_BRUNOAUDRICDASILVAOLIVEIRA.git
    ```

3.  **Instale as Dependências:**
    Execute o comando abaixo para instalar todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a Análise e a Modelagem:**
    Para visualizar a Análise Exploratória dos Dados e todo o processo de criação do modelo, abra e execute o Jupyter Notebook `desafio-lighthouse.ipynb`.
    ```bash
    jupyter notebook desafio-lighthouse.ipynb
    ```
    Dentro deste notebook, você encontrará a resposta para a previsão da nota do IMDB do filme "The Shawshank Redemption".

5.  **(Opcional) Execute o Preditor via Script:**
    O arquivo `main.py` foi configurado para carregar o modelo (`main.pkl`) e realizar previsões. Para executá-lo, utilize o terminal:
    ```bash
    python main.py
    ```
