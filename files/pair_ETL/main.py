
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
df_mergeado

#%%
#creamos la bbdd
bbdd.creacion_bbdd_tablas (sq.query_creacion_bbdd, 'AlumnaAdalab', 'tienda_pair')

#creamos las tablas de la bbdd
# %%
bbdd.creacion_bbdd_tablas (sq.query_creacion_tabla_ventas, 'AlumnaAdalab')
bbdd.creacion_bbdd_tablas (sq.query_creacion_tabla_clientes, 'AlumnaAdalab')
bbdd.creacion_bbdd_tablas (sq.query_creacion_tabla_productos, 'AlumnaAdalab')
bbdd.creacion_bbdd_tablas (sq.query_creacion_productos_ventas, 'AlumnaAdalab')
# %%

# Crear las listas de tuplas con la información a insertar en cada tabla
#%%
# TABLA CLIENTES
datos_tabla_clientes = list(set(zip(df_mergeado["id_cliente"].values, df_mergeado["first_name"].values, df_mergeado["last_name"].values, df_mergeado["email"].values, df_mergeado["gender"].values, df_mergeado["city"].values, df_mergeado["country"].values, df_mergeado["address"].values)))


#%%
# TABLA VENTAS
datos_tabla_ventas = list(set(zip(df_mergeado["id_producto"].values, df_mergeado["id_cliente"].values, df_mergeado["fecha_venta"].values, df_mergeado["cantidad"].values, df_mergeado["total"].values)))
datos_tabla_ventas
#%%
# TABLA PRODUCTOS
datos_tabla_productos = list(set(zip(df_mergeado["id_producto"].values, df_mergeado["nombre_producto"].values, df_mergeado["categoría"].values, df_mergeado["precio"].values, df_mergeado["origen"].values, df_mergeado["descripción"].values)))
datos_tabla_productos
#%%
#TABLA PRODUCTOS VENTAS
datos_tabla_productos_ventas = list(set(zip(df_mergeado["id_producto"].values)))
datos_tabla_productos_ventas

#%%
#insertamos los datos en nuestra bbdd
bbdd.insertar_datos (sq.query_insertar_productos_ventas, 'AlumnaAdalab', 'tienda_pair', datos_tabla_productos_ventas)
#%%
bbdd.insertar_datos (sq.query_insertar_productos, 'AlumnaAdalab', 'tienda_pair', datos_tabla_productos)
#%%
bbdd.insertar_datos (sq.query_insertar_ventas, 'AlumnaAdalab', 'tienda_pair', datos_tabla_ventas)
#%%
bbdd.insertar_datos (sq.query_insertar_clientes, 'AlumnaAdalab', 'tienda_pair', datos_tabla_clientes)
# %%
df_mergeado.columns

