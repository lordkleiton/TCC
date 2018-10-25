#análise de sentimento
import json
import nltk
import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from pandas.io.json import json_normalize

import os                       #navegação de pastas
d = os.path.dirname(os.getcwd())

#pagina web
from flask import Flask, render_template
app = Flask(__name__)

#tweets
dataset = pd.read_csv('{}/dados/csv/dicionario.csv'.format(d))
dataset.count()

tweets = dataset['Text'].values
classes = dataset['Classificacao'].values


vectorizer = CountVectorizer(ngram_range=(1,2))
#vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)

#array a ser testado, se quiser colocar alguma frase pode colocar direto aí
testess = ['Esse governo está no início, vamos ver o que vai dar',
         'Estou muito feliz com o governo de Minas esse ano',
         'O estado de Minas Gerais decretou calamidade financeira!!!',
         'A segurança desse país está deixando a desejar',
         'Repugnante a atitude desse senhor',
         'eu apoio a esse novo governo',
         'espero que esse governo seja repleto de mudanças para melhor',
         'amei essa nova atitude',
         'te amo demais'
        ]

frases_teste = pd.read_json('{}/dados/json/data_file.json'.format(d))

testes = testess

for i in range(0, len(frases_teste)):
        testes.append(frases_teste['textos'][i]['texto'])

#tweets
freq_testes = vectorizer.transform(testes)
a = modelo.predict(freq_testes)

print('\nPredição:')
print('\nClassificação | Frase classificada\n')

for i in range(0, len(testes)):
    print(a[i], ', ', testes[i])

#cross validation
resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

print('\nAcurácia: ', metrics.accuracy_score(classes,resultados))

#estatísticas gerais: precisão, revocação, pontuação f1
sentimento=['Positivo','Negativo','Neutro']
print('\nEstatísticas:\n', metrics.classification_report(classes,resultados,sentimento),'')

#matriz de confusão
print('\nMatriz de confusão:\n', pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True), '\n')

#exige scikit-learn >= 0.20
@app.route('/')
def hello_world():
	estatistica = metrics.classification_report(classes,resultados,sentimento, output_dict=True)
	matriz_conf = pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True)
	return render_template('index.html', estatistica=estatistica, matriz_conf=pd.DataFrame.to_html(matriz_conf), precisao=metrics.accuracy_score(classes,resultados), classificacoes=a, frases=testes)

if __name__ == "__main__":
	app.run(debug=True)
