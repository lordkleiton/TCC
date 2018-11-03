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

#pagina web
from flask import Flask, render_template
app = Flask(__name__)

#função pra ser executada pelo menu
def executa():
	#le o dicionario
	dataset = pd.read_csv('./dados/csv/dicionario.csv')
	dataset.count()

	#pega somente as informações necessárias e separa em 2 listas
	tweets = dataset['Text'].values
	classes = dataset['Classificacao'].values

	#treina o multinomialNB com o dicionario
	vectorizer = CountVectorizer(ngram_range=(1,2))
	freq_tweets = vectorizer.fit_transform(tweets)
	modelo = MultinomialNB()
	modelo.fit(freq_tweets,classes)


	#array a ser testado, se quiser colocar alguma frase pode colocar direto aí
	testes = [
		'Esse governo está no início, vamos ver o que vai dar',
		'Estou muito feliz com o governo de Minas esse ano',
		'O estado de Minas Gerais decretou calamidade financeira!!!',
		'A segurança desse país está deixando a desejar',
		'Repugnante a atitude desse senhor',
		'eu apoio a esse novo governo',
		'espero que esse governo seja repleto de mudanças para melhor',
		'amei essa nova atitude',
	]

	#abre o arquivo de textos salvos previamente
	frases_teste = pd.read_json('./dados/json/data_file.json')

	#divide todos os textos quando encontra . ? ! pra aumentar a quantidade de coisas a serem classificadas
	#e adiciona tudo no vetor a ser classificado
	for i in range(0, len(frases_teste)):
		a1 = frases_teste['textos'][i]['texto'].split(".")
		for j in range(0, len(a1)):
			a2 = a1[j].split("!")
			for k in range(0, len(a2)):
				a3 = a2[k].split("?")
				for l in range(0, len(a3)):
					testes.append(a3[l])


	#faz a predição
	freq_testes = vectorizer.transform(testes)
	a = modelo.predict(freq_testes)


	#imprime tudo na tela
	print('\nPredição:')
	print('\nClassificação | Frase classificada\n')

	for i in range(0, len(testes)):
		print(a[i], ', ', testes[i])


	#cross validation
	resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)

	#imprime acuracia
	print('\nAcurácia: ', metrics.accuracy_score(classes,resultados))

	#estatísticas gerais
	sentimento=['Positivo','Negativo','Neutro']
	print('\nEstatísticas:\n', metrics.classification_report(classes,resultados,sentimento),'')

	#matriz de confusão
	print('\nMatriz de confusão:\n', pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True), '\n')

	#salvando pra poder enviar pelo flask
	estatistica = metrics.classification_report(classes,resultados,sentimento, output_dict=True)
	matriz_con = pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True)
	matriz_conf = pd.DataFrame.to_html(matriz_con)
	precisao = metrics.accuracy_score(classes,resultados)

	#faz o setup da pagina web, exige scikit-learn >= 0.20 pra usar o DataFrame.to_html
	@app.route('/')
	def hello_world():
		return render_template('index.html', estatistica=estatistica, matriz_conf=matriz_conf, precisao=precisao, classificacoes=a, frases=testes)

	#roda o servidor e serve a página web formatada e bonitinha
	app.run()