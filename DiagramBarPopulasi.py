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



plt.title('Populasi Negara ASEAN')
plt.style.use('seaborn')
plt.bar(
    df['Negara'],
    df['Populasi'],
    color = ['lightblue','orange','g','r','magenta','brown', 'pink', 'gray', 'y'],
)

plt.style.use('seaborn')
plt.subplots_adjust(bottom=.21)
plt.grid(True)
plt.legend()
plt.xlabel('Negara')
plt.ylabel('Populasi(x100juta jiwa)')
plt.xticks(rotation=60)
for i,j in enumerate(df['Populasi']):
    plt.text(i-.3, j, str(j), color = 'black', size = 10)
plt.show()