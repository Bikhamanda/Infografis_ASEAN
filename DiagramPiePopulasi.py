import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '17041993', 
    database = 'world',
    auth_plugin = 'mysql_native_password'
)

kursor = dbku.cursor()
querydb = '''select Name as Negara, Population as Populasi, GNP, SurfaceArea as Luas_Daratan from country where region = "SouthEast Asia" order by Name asc'''
kursor.execute(querydb)
x = kursor.fetchall()

df = pd.DataFrame(x, columns= ['Negara', 'Populasi', 'GNP', 'Luas Daratan'])

plt.title('Presentase Penduduk ASEAN')
plt.pie(
    df['Populasi'],
    labels=df['Negara'],
    colors = ['lightblue','orange', 'g','r','magenta','brown', 'pink', 'gray', 'y', 'lightblue', 'b'],
    counterclock = True,
    autopct='%1.1f%%',
    textprops={'color':'k'}
)
plt.show()