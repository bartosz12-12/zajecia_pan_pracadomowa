import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


#zad1
# xlsx =  pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#zad2
# print(df[df['Liczba']<1000])
# print('')
# print(df[df.Imie == 'BARTOSZ'])
# print('')
# suma = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# print(suma)
# print('')
# print(sum(df['Liczba'] & ((df.Rok) > 2004) & ((df.Rok) < 2011) ))
# print('')
# print(sum(df['Liczba'] & ((df.Plec) == 'M') & ((df.Rok) == 2000) ))
# print('')


# zad3

# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
# nazwiska = df['Sprzedawca']
# nazwiska= nazwiska.unique()
# s = pd.Series(nazwiska)
# print(s)
# print('')
# df['Utarg'] = df['Utarg'].astype(float)
# utarg = (df.sort_values(by='Utarg', ascending=False).head(5))
# print(utarg['Utarg'])
# print('')
# print(df.groupby('Sprzedawca').agg({'Sprzedawca':['count']}))
# print('')
# print(df.groupby('Kraj').agg({'Kraj':['count']}))
# print('')
# df['Data zamowienia'] = df['Data zamowienia'].astype('datetime64[ns]')
# polacy = (df[(df.Kraj == 'Polska') & (df['Data zamowienia'].dt.year == 2005)])
# print(polacy.groupby('Kraj').agg({'Utarg':['sum']}))
# print('')

##############             pandas wykresy zdan                 ####################################################

# # zadanie1
# imie = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imie, header=0)
# dziecko = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(dziecko)
# dziecko.plot()
# plt.xticks(np.arange(2000, 2018, step=1))
# plt.xticks(rotation=90)
# plt.show()

#zadanie2

# imie = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imie, header=0)
# dziecko = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(dziecko)
# wykres = dziecko.plot.bar()
# wykres.legend()
# plt.title('Wykres')
# plt.show()

# zad3

# imiona = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(imiona, header=0)
# df = df.groupby(['Rok','Plec']).agg({'Liczba':['sum']})
# df = df.tail(10)
# print(df)
# wykres = df.plot.pie(labels=None, subplots=True, autopct='%.2f %%',
#                      fontsize=10, figsize=(7, 6), legend=(0, 0))
# plt.title('Liczba urodzonych chłopców i dziewczynek w latach 2013-2017')
# plt.legend(labels=df.index, bbox_to_anchor=(1,0.5), loc="center right", bbox_transform=plt.gcf().transFigure)
# plt.tight_layout()
# plt.show()

# zad4

#plt.show()