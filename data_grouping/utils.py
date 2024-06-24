import pandas as pd
import numpy as np


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función agrupa por las columnas
    'state' y 'year' de un dataset dado
    :param df: (pd.DataFrame) dataset a agrupar
    :return: (dict) dataset agrupado en forma de diccionario
    """
    df_grouped = df.groupby(by=['state', 'year'])
    print("Datos agrupados por 'state' y 'year' \n Imprimiendo valores totales")
    print(df_grouped.sum(numeric_only=True))
    return df_grouped


def print_biggest_handguns(df_grouped: pd.DataFrame) -> None:
    """
    Esta función imprime por pantalla el estado y año
    donde más armas de cinto se han registrado
    :param df_grouped: (pd.DataFrame) pd.DataFrame con grupos por estados y años
    :return: None
    """
    max_values = {}
    for grupo, valores in df_grouped:
        max_values[grupo] = valores.loc[:, "handgun"].max()
    # Obtenemos la clave del valor máximo
    max_group = max(max_values, key=max_values.get)
    print(max_group)
    return None


def print_biggest_longguns(df_grouped: pd.DataFrame) -> None:
    """
    Esta función imprime por pantalla el estado y año
    donde más armas largas se han registrado
    :param df_grouped: (pd.DataFrame) diccionario con grupos por estados y años
    :return: None
    """
    max_values = {}
    for grupo, valores in df_grouped:
        max_values[grupo] = valores.loc[:, "long_gun"].max()
    # Obtenemos la clave del valor máximo
    max_group = max(max_values, key=max_values.get)
    print(max_group)
    return None


def groupby_state(df_grouped: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función desagrupa un dataset agrupado por año y estado y lo reagrupa
    solo por año
    :param df_grouped: (pd.DataFrame) dataset agrupado por año y estado
    :return:
    """
    df = df_grouped.obj
    print(df.head())
    df_aux = df.groupby("state")
    print("Dataset agrupado por state! \
    Imprimiendo valores totales por estado")
    print(df_aux.sum().iloc[:5, :])
    return df_aux



