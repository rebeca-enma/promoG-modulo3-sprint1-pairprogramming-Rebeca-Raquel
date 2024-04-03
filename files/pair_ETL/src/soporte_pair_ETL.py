#%%

import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

import warnings
warnings.filterwarnings("ignore")

#%%
def apertura_csv(ruta, quitar_primera_columna=False):
    if quitar_primera_columna:
        df = pd.read_csv(ruta, index_col=0)
    else:    
        df = pd.read_csv(ruta)
    return df

def apertura_csv_error(ruta):
    df = pd.read_csv(ruta, on_bad_lines='warn',index_col=False)
    return df


def cambio_nombre_columnas_df(dataframe):
    dataframe.columns = [col.lower() for col in dataframe.columns]
    print(f"Se ha cambiado el nombre en las columnas del DF {dataframe.name}, actualmente son:\n{dataframe.columns}\n")


def exploracion_df(df):

    print(f"La informacion del DF : _______ {df.name}: ______\n")
    df.info()
    print("__________________________________")


    print(f"El número de filas que tenemos es {df.shape[0]}, y el número de columnas es {df.shape[1]}\n")
    print("__________________________________")

    print(f"El DF {df.name} tiene nulos: \n")
    display(df.isnull().sum())
    print("__________________________________")

    print(f"El DF {df.name} tiene duplicados: {df.duplicated().sum()} \n")
    print("__________________________________")

    print(f"Datos estadisticos del DF {df.name} columnas numericas: \n")
    display(df.describe().T)
    print("__________________________________")

    print(f"Datos estadisticos del DF {df.name} columnas categoricas: \n")
    display(df.describe(include = "object").T)
    print("__________________________________")


def exploracion_col_df(df):


    print(f" _______ {df.name}: ______\n")
    for columna in df.columns:

        print(f" \n----------- ESTAMOS ANALIZANDO LA COLUMNA: '{columna.upper()}' -----------\n")
        print(f"* Nº de datos: {len(df[columna].to_list())}\n")
        print(f"* Frecuencia de valores en la columna: \n {df[columna].value_counts()}\n")
        print(f"* Datos unicos en la columna {len(df[columna].unique())}\n")
        print(f"* Los valores son de tipo: {type(columna)}\n")
        print(f"La suma de datos nulos {df[columna].isnull().sum()}\n")
        print(f"La suma de datos duplicados {df[columna].duplicated().sum()}\n")
        # print(df[columna].unique()) 


def union_datos(df1,df2,df3):

    mergeado_inner = df1.merge (df2, left_on = 'id', right_on = 'id_cliente', how = 'left')
    final =  mergeado_inner.merge (df3, left_on = 'id_producto', right_on = 'id', how = 'left')
    final.to_csv('files/csv_merged.csv')
    
    return final

# %%
