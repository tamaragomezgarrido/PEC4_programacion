import pandas as pd
import regex as re


def find_max_col(df, filtercol: str, cols_to_return: list,):
    """Dando el nombre de un dataframe, una columna sobre la que
    calcular el máximo y una lista de columnas a devolver,
    esta función devuelve las filas
    de las columnas indicadas para las que el valor indicado es máximo.

    Parámetros:
    df: dataframe. Nombre del dataframe
    filtercol: string. Columna de la que se calcula el valor máximo.
    cols_to_return: lista. Columnas de las que se devolverán las filas
    con valor máximo de filtercol.

    Devuelve: dataframe.
    """

    df = pd.DataFrame(df)
    maximo = df[filtercol].max()
    resultado = df.loc[(df[filtercol] == maximo), cols_to_return]

    return resultado


def find_rows_query(df, query: tuple,
                    cols_to_return: list):
    """Permite realizar filtros avanzados.

    Parámetros:

    df: dataframe. Nombre del dataframe

    query: tupla. 1er elemento: lista de columnas sobre las que queremos filtrar.
    2o elemento: lista de valores que queremos usar en el filtro.
    Si la columna es categórica los valores serán tipo string.
    Si la columna es numérica los valores serán tipo numérico.

    cols_to_return: lista. Columnas de las que se devolverán las filas con los
    valores indicados en la query.

    Devuelve: dataframe.
    """

    filtrar = query[0]
    valores = query[1]
    data = df
    for i in range(len(filtrar)):
        if df[filtrar[i]].dtype != int:
            condicion = str(filtrar[i]) + '==' + str(valores[i])
            condicion = str(condicion)
        else:
            condicion = str(valores[i][0])+'<='+str(filtrar[i])+'<='+str(valores[i][1])

        data_query = data.query(condicion)

    data_query = data.loc[:, cols_to_return]

    return data_query


def calculate_BMI(df, gender: str, year: int, cols_to_return: list):
    """Calcula el BMI de los jugadores de un dataframe, género y año dado.

        Parámetros:

        df: dataframe. Nombre del dataframe
        gender: string. 'M': masculino. 'F': femenino.

        cols_to_return: lista. Columnas de las que se devolverán las filas,
        además de la columna 'BMI'.

        Devuelve: dataframe.
        """
    datos = df.loc[(df['gender'] == gender) & (df['year'] == year)]
    datos['height_m'] = datos['height_cm'] / 100
    datos['BMI'] = datos['weight_kg'] / (datos['height_m'] * datos['height_m'])
    lista = cols_to_return
    lista.append('BMI')
    datos_BMI = datos.loc[:, lista]

    return datos_BMI


def get_flag(df):
    """Añade el código del país al dataframe..

        Parámetros:

        df: dataframe. Nombre del dataframe

        Devuelve: dataframe con la columna 'flag' con el código del país.
        """
    patron = '\([a-z]+)\.png'
    club_flag = df['club_flag_url']
    flag_list = []
    for i in club_flag.index:
        flag = re.findall(patron, i)
        flag_list.append(flag[0])
    df['flag'] = flag_list

    return df