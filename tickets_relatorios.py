import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
plan = Workbook(r"C:\Users\luiss\Downloads\tickets.xlsx")
#planilha tirada do sistema de ticket WordPress
#plan = pd.read_excel (r"C:\Users\luiss\Downloads\tickets.xlsx")
Planilha1 = plan.active
color = plan._colors.index('master')

print(color)


""" for row in range(Planilha1):
    print(Planilha1.row(row))
 """



""" cont = 0
def calcule():
    if planilha['status'].values == "status":
        cont += 1
        print(cont)
    else:
        print("erro!!!")
    retorn

print(calcule()) """