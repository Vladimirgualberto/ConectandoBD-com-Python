# Conectando no Banco de dados com Python

Neste artigo vamos aprender de forma simples como conectar no banco de dados com python.

## Primeiro passo
Vamos precisar importar a biblioteca sqlalchemy para conexão com banco de dados, e vamos utilizar a biblioteca pandas, a ideia é conectar no banco de dados e armazenar essa busca em uma estrutura de dataframe.

```
import sqlalchemy
import pandas as pd
```
## Segundo passo
Vamos agora definir uma função em python e para isso definimos utilizando a seguinte construtor:

```
def nome_da_funcao(Parametros de entrada):

return
```
Detalhe importante, a função pode ou não ter algum retorno, no nosso exemplo iremos ter dois parametros de entrada, executar o select dentro do bando de dados e salvar em um dataframe, logo essa função retorna um dataframe

```
def conectabd(ip, data):
    engine = sqlalchemy.create_engine( 'mysql+pymysql://user:password@'+ip+':3306/database')
    sql = "SELECT * duration FROM nomedobanco.tabela where calldate >= '"+data+" 00:00:01' and calldate <= '"+data+" 23:59:59'"
    df = pd.read_sql(sql,engine)
    return df
```

No exemplo temos então a função definida com nome de conectabd e com dois parametros de entrada, o primeiro o ip de destino, que é o local onde o bando de dados está em execução e o segundo é um parametro de data que vai informar qual período ou data será realizado no select.

Vamos agora detalhar linha a linha do corpo da função, na primeira linha temos:
engine = sqlalchemy.create_engine( 'mysql+pymysql://user:password@'+ip+':3306/database')

a váriável engine expressa a string de conexção do banco de dados, invocando a função create_engine da lib sqlalchemy, como parametros temos a string informando o motor de conexão do slq e python, neste caso definido por 'mysql+pymysql', em seguinda o nome do usuário de conexão com banco de dados definido por "user" seguido de :password que representa a senha(neste caso o administrador do banco de dados deve criar um usuário e senha de acesso ao banco de dados) concatenado com @+ip+, neste caso estamos montando a string baseada na variável de entrada ip, de forma mais direta teremos o seguinte exemplo: mysql+pymysql://user:password@192.168.1.10:3306 e por fim o database representa a instância ou nome do banco de dados.

Na segunda linha temos:

sql = "SELECT * duration FROM nomedobanco.tabela where date >= '"+data+" 08:00:00' and date <= '"+data+" 21:00:0'"

a variável sql armazena a string de select no banco de dados, selecionando as informações baseado em uma data específica (neste caso estamos definindo uma data fixa ,por exemplo, "2020-12-31" e estamos definindo um horário de busca fixa, logo esse exemplo trará do banco de dados informações do dia 31 do dezembro de 2020 com horário entre 8 horas e 21 horas.

Por fim, na terceira linha temos:

df = pd.read_sql(sql,engine)

Estamos agora armazenando a busca em um dataframe e para isso precisamos passar a string de busca "sql" e a engine de conexão "engine)
e com isso essa função retorna um dataframe ao ser invocada, return df.

Bom é isso, até a próxima =)

