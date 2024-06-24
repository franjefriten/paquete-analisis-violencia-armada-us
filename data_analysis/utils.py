import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import selenium as sl
import folium as fl
import io
from PIL import Image


def time_evolution(df: pd.DataFrame) -> plt.figure:
    """
    Crea una figura de evolución temporal de permit,
    hand_gun y long_gun
    :param df: (pd.DataFrame) dataframe con los datos a dibujar
    :return: (plt.figure) figura de serie temporal
    """
    df_grouped = df.groupby('year').sum().reset_index()
    fig, ax = plt.subplots()
    fig.suptitle("Serie temporal de permit, handgun, long_gun")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Registros")
    plt.xticks(rotation=45)
    ax.plot(df_grouped.year, df_grouped.handgun, color='r', label="handgun")
    ax.plot(df_grouped.year, df_grouped.long_gun, color='b', label="long_gun")
    ax.plot(df_grouped.year, df_grouped.permit, color='g', label="permit")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Registros")
    ax.legend()
    fig.savefig("time_evolution.png")


def calculate_relative_values(df: pd.DataFrame):
    df["permit_perc"] = (df['permit'] * 100 / df['pop_2014'])
    df["handgun_perc"] = (df['handgun'] * 100 / df['pop_2014'])
    df["longgun_perc"] = (df['long_gun'] * 100 / df['pop_2014'])
    print("Valores porcentuales creados!")
    return df


def analyze_permit(df_merged: pd.DataFrame):
    media_permit_perc = df_merged.permit_perc.mean()
    print("Media permit_perc:", media_permit_perc)
    print("Info Kentucky:", df_merged[df_merged.state == "Kentucky"])
    df_merged.loc[df_merged.state == "Kentucky", "permit_perc"] = media_permit_perc
    print("Media Kentucky alterada")
    nueva_media_permit_perc = df_merged.permit_perc.mean()
    print("Nueva media permit_perc:", nueva_media_permit_perc)


def create_choropleth_maps(df: pd.DataFrame, col: str) -> None:
    """
    Esta función crea mapas coropléticos basados en estados unidos
    :param df: (pd.DataFrame) Dataframe con los datos a dibujar y
    los nombres de los estados
    :param col: (str) columna con los datos a dibujar
    :return: None
    """
    cols = ["code", "year", "permit_perc", "handgun_perc", "longgun_perc"]
    df = df[cols]
    df = pd.DataFrame(
        data = pd.merge(
            df.code,
            df.groupby(by='code').sum()[["permit_perc", "handgun_perc", "longgun_perc"]] * len(df) / 100,
            on='code'
        )
    )
    m = fl.Map(location=[40, -95], zoom_start=4)
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data"
    )
    state_geo = f"{url}/us-states.json"
    fl.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=df,
        columns=["code", col],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=f"Porcentaje de {col} total (%) a lo largo del tiempo",
    ).add_to(m)
    fl.LayerControl().add_to(m)
    m.save(f'imagen_{col}.html')