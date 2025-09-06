import pickle
import pandas as pd

# Carregar o modelo já treinado
with open('main.pkl', 'rb') as file:
    modelo = pickle.load(file)


#A variavel predição recebe o filme a ser previsto o IMDB
filmePredicao = {'Series_Title': 'The Shawshank Redemption',
 'Released_Year': '1994',
 'Certificate': 'A',
 'Runtime': '142 min',
 'Genre': 'Drama',
 'Overview': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
 'Meta_score': 80.0,
 'Director': 'Frank Darabont',
 'Star1': 'Tim Robbins',
 'Star2': 'Morgan Freeman',
 'Star3': 'Bob Gunton',
 'Star4': 'William Sadler',
 'No_of_Votes': 2343110,
 'Gross': '28,341,469'}

#Esta função realiza a limpeza dos dados do filme que precisa ser previsto como no tópico 2 deste notebook, retorna um Dataframe para predição
def limpezaDaEntrada(filme):
    filme['Gross'] = int(filme['Gross'].replace(',', ''))
    
    predicaoDf = pd.DataFrame([{
        'Meta_score': filme['Meta_score'],
        'No_of_Votes': filme['No_of_Votes'],
        'Gross': filme['Gross']
    }])
    return predicaoDf

#Chama a função limpezaDaEntrada e Guarda numa variavel
filmeTeste = limpezaDaEntrada(filmePredicao)

predicao = modelo.predict(filmeTeste)[0]

print(f"Nota para '{filmePredicao['Series_Title']}': {predicao:.1f}")
