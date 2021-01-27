import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd


def conectabd(ip, data):
    engine = sqlalchemy.create_engine( 'mysql+pymysql://user:password@'+ip+':3306/database')
    sql = "SELECT calldate, src, realdst,disposition, duration FROM nipcdr.a_cdr where calldate >= '"+data+" 00:00:01' and calldate <= '"+data+" 23:59:59'"
    df = pd.read_sql(sql,engine)
    return df
