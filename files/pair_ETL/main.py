
#%%
from src import soporte_pair_ETL as sp
from src import soporte_queries_pair_ETL_2 as sq
from src import bbdd_soporte as bbdd
import pandas as pd

# %%
df_clientes = sp.apertura_csv('files/clientes.csv',True)
df_clientes.name = "Clientes"


df_ventas = sp.apertura_csv('files/ventas.csv')
df_ventas.name = "Ventas"

df_productos = sp.apertura_csv_error('files/productos.csv')
df_productos.name = "Productos"

sp.cambio_nombre_columnas_df(df_clientes)
sp.cambio_nombre_columnas_df(df_ventas)
sp.cambio_nombre_columnas_df(df_productos)


## "Impresion" DF´s
display(df_clientes)
display(df_ventas)
display(df_productos)

# %%
## Exploracion DF´s
sp.exploracion_df(df_clientes)
df_clientes.duplicated(subset=["first_name","last_name"]).sum()
sp.exploracion_df(df_ventas)
sp.exploracion_df(df_productos)

# %%
## Exploracion columnas
sp.exploracion_col_df(df_clientes)
sp.exploracion_col_df(df_ventas)
sp.exploracion_col_df(df_productos)


# %%

## Union DF
df_mergeado = sp.union_datos(df_clientes,df_ventas,df_productos)

#creamos las tablas en nuestra bbdd
bbdd.creacion_bbdd_tablas (sq.query_creacion_bbdd, 'AlumnaAdalab', 'tienda_pair')
# %%
bbdd.creacion_bbdd_tablas (sq.query_creacion_tabla_ventas, 'AlumnaAdalab')
bbdd.creacion_bbdd_tablas (sq.query_creacion_tabla_clientes, 'AlumnaAdalab')
bbdd.creacion_bbdd_tablas (sq.query_creacion_tabla_productos, 'AlumnaAdalab')
bbdd.creacion_bbdd_tablas (sq.query_creacion_productos_ventas, 'AlumnaAdalab')
# %%
#insertamos las tablas
bbdd.insertar_datos (sq.query_insertar_productos_ventas, 'AlumnaAdalab', 'tienda_pair')
bbdd.insertar_datos (sq.query_insertar_productos, 'AlumnaAdalab', 'tienda_pair')
bbdd.insertar_datos (sq.query_insertar_ventas, 'AlumnaAdalab', 'tienda_pair')
bbdd.insertar_datos (sq.query_insertar_clientes, 'AlumnaAdalab', 'tienda_pair')
# %%
df_mergeado.columns

#%%
datos_tabla_productos_ventas = list(set(zip(df_mergeado["uri_cancion"].values, df_mergeado["song"].values)))