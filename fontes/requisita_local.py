import requests                 #requests
from bs4 import BeautifulSoup   #limpa o texto
import json                     #json
import os                       #navegação de pastas

#pega o endereço da pasta
d = os.path.dirname(os.getcwd())

#vai virar o json a ser salvo
textos = {
    "textos" : []
}

#pega o token de acesso
def postTokenUsuario(login, password):
    payload = {'grant_type':'password', 'login':login, 'password': password}
    r = requests.post('http://solar.virtual.ufc.br/oauth/token', payload)

    access_token = r.json()['access_token']
    print('token de acesso:\n', access_token)

    getUserGroups(access_token)

#pega todos os grupos que o usuario tem
def getUserGroups(access_token):
    payload = {'access_token':access_token}
    r = requests.get('http://solar.virtual.ufc.br/api/v1/curriculum_units/groups/', payload)
    r = r.json()

    for i in range(0, len(r)):
        print('nome da turma: ', r[i]['name'])
        groups = r[i]['groups']
        print('grupos:\n', groups)
        for j in range(0, len(groups)):
            group_id = groups[j]['id']
            print('id do grupo:\n', group_id)
            getForumID(access_token, group_id)

#pega todos os id de forum que o usuario tem
def getForumID(access_token, group_id):
    payload = {'access_token':access_token}
    r = requests.get('http://solar.virtual.ufc.br/api/v1/groups/{}/discussions/'.format(group_id), payload)
    r = r.json()

    for i in range(0, len(r)):
        forum_id = r[i]['id']
        print('id do forum:', forum_id)
        getForumContent(access_token, group_id, forum_id)

#pega todos os textos de forum do usuario
def getForumContent(access_token, group_id, forum_id):
    payload = {'access_token':access_token, 'group_id':group_id}
    r = requests.get('http://solar.virtual.ufc.br/api/v1/discussions/{}/posts/'.format(forum_id), payload)
    r = r.json()

    for i in range(0, len(r)):
        texto = BeautifulSoup(r[i]['content'].encode('utf-8', 'ignore'), features="lxml").text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('\xa0', ' ')
        textos['textos'] = [
            {
                "ordem": i,
                "forum_id": forum_id,
                "texto": texto
            }
        ] + textos['textos']    


#abre o json de login
with open('{}/dados/json/login.json'.format(d)) as f:
    login = json.load(f)

#executa
for i in range(0, len(login)):
    postTokenUsuario(login[i]['login'], login[i]['senha'])

#salva o json de textos
with open("{}/dados/json/data_file.json".format(d), "w") as write_file:
    json.dump(textos, write_file, indent=4)

#imprime os textos coletados na tela
for i in range(0, len(textos['textos'])):
    print('\ntexto:\n', textos['textos'][i]['texto'])

