
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import and_, or_, not_

from sqlalchemy import desc, asc

engine = create_engine('postgresql://postgres:@localhost/sqlalchemy')
metadata = MetaData()

# users
users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('age', Integer),
    Column('country', String(20),nullable=False),
    Column('email', String(50),nullable=False),
    Column('gender', String(6), nullable=False),
    Column('name', String(50), nullable=False),
)

if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    with engine.connect() as connection:
        # abriendo users.json
        with open('users.json') as file:            
            # Cargando la tabla con los usuarios
            connection.execute(users.insert(), json.load(file))
        
        # Actualizando un registro
        # update_query = users.update(users.c.id == 1).values(
        #     name = 'Cambio de nombre'
        # )
        # Actualizando todos los registros
        # update_query = users.update().values(
        #     name = 'Cambio de nombre'
        # )
        
        # Actualizando con update
        update_query = update(users).values(
            name='Nuevo cambio de nombre 2.0'
        ).where(
            users.c.id == 20
        )
        
        print(update_query)
        
        result = connection.execute(update_query)
        print(
            result.rowcount
        )
        