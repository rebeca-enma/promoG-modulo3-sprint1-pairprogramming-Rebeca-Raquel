
#%%
from src import soporte_pair_ETL as sp

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


# %%

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


