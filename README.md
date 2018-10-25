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

No terminal vai aparecer uma espécie de menu, onde você pode digitar **1** para fazer as requisições de textos baseadas nas contas que inseriu no `login.json`, **2** para fazer a análise dos textos que foram capturados no primeiro passo, ou **q** para sair

Ao selecionar **1**, se algum dos usuários tiver uma conta ativa e com disciplinas ativas no SOLAR, será criado um arquivo JSON chamado `data_file.json` na pasta `/dados/json` onde se encontram todos os textos escritos nos fóruns que o usuário tem acesso. 

Ao selecionar **2**, o terminal será preenchido de informações, como a classificação das frases, estatísticas da análise e matriz de confusão. Essa forma de visualização é nenhum pouco interessante, mas achei necessária de manter. Para uma real visualização das informações, basta seguir o link `http://127.0.0.1:5000` que o navegador será aberto com a página correta.
