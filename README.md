# TCC
Meu TCC, feito totalmente em python3 (mais especificamente 3.7.0), que usa os textos obtidos do AVA SOLAR para fazer a Análise de Sentimento via Multinomial Naive Bayes

# Requisitos
[Anaconda](https://www.anaconda.com/download/)
  - No meu caso usei a versão `5.3.0`

# Como instalar
É preciso clonar esse repositório numa pasta qualquer que você deseje usar

Depois, abra um terminal na raiz da pasta do projeto e digite `pip install -r requirements.txt`

# Como configurar
Na pasta `/dados/json`, crie um arquivo chamado `login.json` e siga o modelo já disponível no arquivo `login_sample.json`. Caso prefira, disponibilizo aqui mesmo em seguida a estrutura para copiar e colar.

```json
[
    {
        "login" : "logindousuario1aqui",
        "senha" : "senhadousuario1aqui"
    },
    {
        "login" : "logindousuario2aqui",
        "senha" : "senhadousuario2aqui"
    }
]
```

# Como usar
Basta abrir o terminal e digitar `python menu.py`

Ao fazer isso, se algum dos usuários tiver uma conta ativa e com disciplinas ativas no SOLAR, será criado um arquivo JSON chamado `data_file.json` na pasta `/dados/json` onde se encontram todos os textos escritos nos fóruns que o usuário tem acesso. 
