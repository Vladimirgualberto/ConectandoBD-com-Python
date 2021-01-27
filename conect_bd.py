import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd


def conectabd(ip, data):
    engine = sqlalchemy.create_engine( 'mysql+pymysql://user:password@'+ip+':3306/database')
    sql = "SELECT * FROM nomedobanco.tabela where date >= '"+data+" 08:00:00' and date <= '"+data+" 21:00:00'"
    df = pd.read_sql(sql,engine)
    return df
