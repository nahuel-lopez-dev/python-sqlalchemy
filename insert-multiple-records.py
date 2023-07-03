import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

engine = create_engine('postgresql://postgres:@localhost/sqlalchemy')
metadata = MetaData()

# users
users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('age', Integer()),
    Column('Country', String(20), nullable=False),
    Column('email', String(50), nullable=False),
    Column('gender', String(6), nullable=False),
    Column('name', String(50), nullable=False),
)

# "age": "24",
# "country": "Brazil",
# "email": "user7@example.com",
# "gender": "female",
# "name": "Isabella Martinez"

if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    # trabajando con un contexto. Se evita connection.close()
    with engine.connect() as connection:
        
        insert_query = users.insert() # Query -> Insert into users
        # leyendo el archivo
        with open('users.json') as file:
            # convertiendo el contenido a un listado de diccionarios
            users = json.load(file)
            # ejecutando la sentencia una sola vez 
            # y pasando el diccionario de users
            connection.execute(insert_query, users)
            
            ##### No conviene esta forma
            # iterando sobre cada uno de los elementos
            # se establece los valores dentro del insert
            # pasando como parámetros las llaves del diccionario
            # for user in users:
            #     query = insert_query.values(**user)
            #     # ejecutando la sentencia
            #     connection.execute(query)
    
    

