import pandas as pd
from data_fetching.utils import read_csv


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta columna toma la fecha de la columna
    'month' en formato (2020-2)
    y crea dos nuevas 'year' y 'month'
    :param df: dataframe a alterar
    :return: dataframe alterado
    """
    date = pd.to_datetime(df['month'], format="%Y-%m")
    df["year"] = date.dt.year
    df["month."] = date.dt.month
    print("Columnas 'year' y 'month' creadas \n")
    print(df.iloc[:5, :])
    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función elimina la columna 'month' del dataframe
    :param df: (pd.DataFrame) dataset con la columna 'month'
    :return: (pd.DaraFrame) dataset son la columna 'month'
    """
    if 'month' not in df.columns:
        raise KeyError('Columna month no hallada')
    else:
        df = df.drop(columns=["month"])
        df = df.rename(columns={"month.": "month"})
        print("Columnas alteradas exitosamente \n")
        print(f"Columnas: {df.columns} \n")
        print(df.iloc[:5, :])
        return df


def merge_datasets(df: pd.DataFrame, file_uspop: str):
    df_us_pop = read_csv(file_uspop)
    df_merged = pd.merge(df, df_us_pop, on='state')
    df_merged.reset_index()
    print("Datasets fusionados")
    print(df_merged.iloc[:5, :])
    return df_merged
