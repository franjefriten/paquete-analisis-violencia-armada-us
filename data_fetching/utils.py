import pandas as pd


def read_csv(file: str) -> pd.DataFrame:
    """
    Esta función lee un archivo csv
    :param file: (str) dirección de memoria del csv
    :return: (pd.DataFrame) pandas dataframe
    """
    try:
        df = pd.read_csv(file)
        print(f"Archivo {file} cargado! \n")
        print(df.iloc[:5, :])
        return df
    except FileNotFoundError as e:
        print(type(e).__name__, f"Archivo no encontrado en {file}")


def clean_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Esta función limpia el dataframe. Elimina las columnas
    innecesarias y se queda con month, state, permit, handgun, long_gun
    :param df: (pd.DataFrame) dataframe pandas a limpiar
    :return: (pd.DataFRame) dataframe pandas limpio
    """
    try:
        cols = ['month', 'state', 'permit', 'handgun', 'long_gun']
        df_clean = df[cols]
        print("Dataset limpio! \n")
        print(df_clean.columns)
        return df_clean
    except KeyError:
        print(f"Error en la limpieza del dataset, \
        columnas {cols} no encontradas en {df.columns}")


def rename_cols(df: pd.DataFrame, oldcol: str, newcol: str) -> pd.DataFrame:
    """
    Esta función renombre columnas del dataset una a una.
    :param df: (pd.DataFrame) dataset para cambiar nombres de columnas
    :param oldcol: (str) nombre de la columna antigua
    :param newcol: (str) nombre de la columna nueva
    :return: (pd.DataFrame) dataset con los nombres nuevos de las columnas
    """
    if oldcol not in df.columns:
        raise KeyError(f"Columna {oldcol} no encontrada")
    else:
        df = df.rename({oldcol: newcol})
        print(f"Columna {oldcol} cambiada a {newcol}")
        print(df.columns)
        return df


def clean_states(df_grouped: pd.DataFrame):
    df = df_grouped.obj
    not_states = ["Guam", "Virgin Islands", "Puerto Rico", "Mariana Islands"]
    if any(map(lambda x: x in df.state.unique(), not_states)):
        df = df.drop(df[df.state.isin(not_states)].index)
        return df.groupby(by='state')
    else:
        return 0
