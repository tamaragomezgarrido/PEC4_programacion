import pandas as pd
import re
import matplotlib.pyplot as plt
from create_data import read_add_year_gender, join_male_female, join_datasets_year
from utils import find_max_col, find_rows_query, get_flag, calculate_BMI

if __name__ == '__main__':
    #Ejercicio 1.a)
    print('Ejericio 1.a')
    print('Obtener los datos de las jugadoras de 2016')
    data1a = read_add_year_gender('data', 'F', 2016)
    print(data1a.head())

    #Ejercicio 1.b)
    print('\nEjercicio 1.b')
    print('Obtener los datos de futbolistas masculinos y femeninos en 2017')
    data1b = join_male_female('data', 2017)
    print('Los géneros del dataframe son:')
    print(data1b['gender'].unique())
    print('Los años recogidos en el dataframe son:')
    print(data1b['year'].unique())

    #Ejercicio 1.c)
    print('\nEjercicio 1.c')
    print('Obtener los datos de los futbolistas de ambos géneros en 2017,2019 y 2021')
    data1c = join_datasets_year('data', [2017,2019,2021])
    print('Los géneros recogidos en el dataframe son:')
    print(data1c['gender'].unique())
    print('Los años recogidos en el dataset son:')
    print(data1c['year'].unique())
    print('El número total de jugadores que aparece en el dataset es:')
    print(data1c.shape[0])

    #Ejercicio 2.a)
    print('Ejercicio 2.a')
    print('Obtener el nombre, la edad, y el club en el que juegan las jugadoras con máxima puntuación overall en 2021')
    data_2021 = read_add_year_gender('data','F',2021)
    data2a = find_max_col(data_2021, 'overall', ['short_name', 'age', 'club_name', 'overall'])
    print(data2a)

    #Ejercicio 2.c)
    print('Ejercicio 2.c.1')
    print('Mostrad por pantalla el short_name, year, age, overall y potential de:'
          'jugadores de nacionalidad belga menores de 25 años con máximo potencial en'
          'futbol masculinio')
    jugadores = join_datasets_year('data',[2016,2017,2018,2019,2020,2021,2022])
    maximo_potencial = find_max_col(jugadores,'potential',['short_name','year','age','overall','potential','country','gender'])
    print(maximo_potencial)

    #Ejercicio 3a)
    print('Ejercicio 3.a')
    data3a = read_add_year_gender('data', 'M', 2022)
    data3a_bmi = calculate_BMI(data3a, 'M', 2022, ['club_flag_url', 'BMI'])
    print(data3a_bmi)

    #Ejercicio 3.b)
    print('Ejercicio 3.b')
    print('Mostrad un gŕafico con el BMI máximo por país. Masculino, 2022')
    data3b = read_add_year_gender('data', 'M', 2022)
    data_3b_flag = get_flag(data3b)
    grafico = data_3b_flag.groupby('flag').agg({'BMI' : 'max'})
    print(grafico.plot(kind='bar'))


