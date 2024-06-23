import data_fetching.utils as data_fetch
import data_processing.utils as data_process
import data_grouping.utils as data_group
import data_analysis.utils as data_analyze
import os

## EJERCICIO 1

CWD = os.getcwd()
RUTA_ARMAS = r"data/nics-firearm-background-checks.csv"
RUTA_USPOP = r"data/us-state-populations.csv"

## EJERCICIO 1.1

df = data_fetch.read_csv(os.path.join(CWD, RUTA_ARMAS))

## EJERCICIO 1.2

df = data_fetch.clean_csv(df)

## EJERCICIO 1.3

df = data_fetch.rename_cols(df, newcol="long_gun", oldcol="long_gun")

## EJERCICIO 2

## EJERCICIO 2.1

df = data_process.breakdown_date(df)

## EJERCICIO 2.2

df = data_process.erase_month(df)

## EJERCICIO 3

## EJERCICIO 3.1

df_grouped = data_group.groupby_state_and_year(df)

## EJERCICIO 3.2

data_group.print_biggest_handguns(df_grouped=df_grouped)

## EJERCICIO 3.3

data_group.print_biggest_longguns(df_grouped=df_grouped)

## EJERCICIO 4

## EJERCICIO 4.1

data_analyze.time_evolution(df)

## EJERCICIO 4.2

"""
Podemos observar que salvo el periodo de 2012-2013 donde hubo un
aumento puntual de armas largas, el aumento de la expedición de 
permisos de armas se debe, principamente, a una tendencia en incremento
de la compra de armas cortas o de cinto, véase pistolas, revólveres, etc.
Esta tendencia decayó enormemente en 2020 con la pandemia como cabe esperar
"""

## EJERCICIO 5

## EJERCICIO 5.1

df_grouped = data_group.groupby_state(df_grouped=df_grouped)

## EJERCICIO 5.2

df_grouped = data_fetch.clean_states(df_grouped=df_grouped)

## EJERCICIO 5.3

df_merged = data_process.merge_datasets(df, file_uspop=os.path.join(CWD, RUTA_USPOP))

## EJERCICIO 5.4

df_merged = data_analyze.calculate_relative_values(df_merged)

## EJERCICIO 5.5

data_analyze.analyze_permit(df_merged)
