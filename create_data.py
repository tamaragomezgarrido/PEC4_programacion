import pandas as pd


def read_add_year_gender(filepath: str, gender: str, year: int):
    """Dando un directorio, género, y año se obtienen los datos de los
    jugadores o jugadoras de ese año, y se añade al conjunto de datos
    el año y el género del jugador/a.

    Parámetros:
    filepath: string. Ruta del archivo.
    gender: string. Género del jugador. 'M' : masculino. 'F': femenino,
    year: integer. Año en formato XXXX.

    Devuelve: dataframe.
    """

    if gender == 'F':
        x = 'female_'
    else:
        x = ''

    if year == 2016:
        y = '16'
    elif year == 2017:
        y = '17'
    elif year == 2018:
        y = '18'
    elif year == 2019:
        y = '19'
    elif year == 2020:
        y = '20'
    elif year == 2021:
        y = '21'
    elif year == 2022:
        y = '22'
    else:
        print('Error. Debe insertar un año entre 2016 y 2022')

    url = filepath + '/' + x + 'players_' + y + '.csv'

    df = pd.read_csv(url)
    df['gender'] = gender
    df['year'] = year

    return df


def join_male_female(filepath: str, year: int):
    """Dando una ruta de archivo y año se obtienen los datos de todos los
    jugadores y jugadoras de ese año, y se añade al conjunto de datos
    el año y el género que corresponde a cada futbolista.

    Parámetros:
    filepath: string. Ruta del archivo.
    year: integer. Año en formato XXXX.

    Devuelve: dataframe.
    """

    if year == 2016:
        y = '16'
    elif year == 2017:
        y = '17'
    elif year == 2018:
        y = '18'
    elif year == 2019:
        y = '19'
    elif year == 2020:
        y = '20'
    elif year == 2021:
        y = '21'
    elif year == 2022:
        y = '22'
    else:
        print('Error. Debe insertar un año entre 2016 y 2022')

    female = pd.read_csv(filepath + '/' + 'female_players_' + y + '.csv')
    male = pd.read_csv(filepath + '/' + 'players_' + y + '.csv')
    female['gender'] = 'F'
    male['gender'] = 'M'
    female['year'] = year
    male['year'] = year
    join_df = pd.concat([female, male], sort=False)

    return join_df


def join_datasets_year(filepath: str, years: list):
    """Dando una ruta de archivo y una lista de años se obtienen los datos
    de todos los jugadores y jugadoras de los años indicados,
    devolviendo un único dataframe que contiene
    información sobre el género y año al que corresponden
    los datos de cada futbolista.

    Parámetros:
    filepath: string. Ruta del archivo.
    year: lista. Años en formato XXXX.

    Devuelve: dataframe.
    """

    lista = []

    for year in years:
        df = join_male_female(filepath, year)
        lista.append(df)

    data_join = pd.concat(lista)

    return data_join

