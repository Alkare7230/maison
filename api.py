#coding:utf-8

from pandas.io import sql
from sqlalchemy import create_engine
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Salut tout el monde c'est david larfarge pokémon, aujourd'hui on se retrouve pour une vidéo un peu spécial avec miss shirashi"

if __name__ == "__main__":
    app.run()



engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(user="",
                               host='',
                               pw="",
                               db=""))
connection = engine.connect()
recherche='bar à cocktail 33130 '
query = "SELECT * FROM Lieu WHERE preference =%s"
result = connection.execute(query, (recherche, ))
for row in result:
    print (row[0])
    print (row[1])
    print (row[2])
connection.close()
engine.dispose()