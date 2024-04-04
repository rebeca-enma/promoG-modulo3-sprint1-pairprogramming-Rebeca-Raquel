#%%
from src import soporte_queries_pair_ETL_2 as sq
from src import bbdd_soporte as bbdd
import pandas as pd



# %%
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

#%%
df = pd.read_csv ('files/csv_merged.csv', index_col = 0)
df.head()
# %%
datos_tabla_productos_ventas = list(set(zip(df_final["uri_cancion"].values, df_final["song"].values)))

