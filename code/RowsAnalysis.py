import pandas as pd
import numpy as np


class RowsAnalysis:
    """
        FUNCIONES PARA:
            + LEER LA CANTIDAD DE COLUMNAS COLUMNAS
            + LEER LOS NULO POR COLUMNA
    """

    def rows_csv(df):
        """
        DEVUELVE EL NUMEO DE COLUMNAS DEL CSV
        :param df: el DataFrame del que queremos obtener las columnas
        :return: las columnas
        """
        size = df.shape
        print(f'(filas, columnas) = {size}')
        columns = size[1]
        print('NUMERO COLUMNAS ----- EXITO')
        return columns

    def read_number_of_null_values(df):
        """
        LEER EL NUMERO DE VALORES NULOS DE LAS COLUMNAS DEL CSV
        :param df: el DataFrame del que queremos obtener los nulos de las columnas
        :return: numero de nulos por columnas
        """
        number_of_null_values = df.isnull().sum()
        print(number_of_null_values.sort_values())
        print('NULOS COLUMNAS ----- EXITO')
        return number_of_null_values

    def delete_null_columns(df):
        """
        ELIMINAR LAS COLUNAS CON MAS DEL 50% DE VALORES NULOS
        :param df: el DataFrame del que queremos eliminar las columnas
        """
        for column in df:
            if df[column].isnull().sum() > len(df.index) * 50 / 100:
                del df[column]
        print('BORRADO COLUMNAS NULAS  ----- EXITO' + '\n')

    def select_columns(df):
        """
        ELIMINAR COLUMNAS QUE NO VAMOS A USAR PARA QUEDARNOS CON LAS QUE QUEREMOS
        :return: el DataFrame con las columnas que queremos
        """
        list_columns_want = ['iyear', 'eventid', 'iyear', 'imonth', 'iday',	'country_txt', 'region_txt', 'provstate',
                             'city', 'latitude', 'longitude', 'success', 'attacktype1_txt', 'targtype1_txt', 'gname',
                             'weaptype1_txt']
        # [column for column in list_columns_want if df[column] not in list_columns_want]
        for column in df:
            if column not in list_columns_want:
                del df[column]
            else:
                print('I WANT THIS, NEXT COLUMN')
        print('SELECCION COLUMNAS  ----- EXITO' + '\n')
        return df
