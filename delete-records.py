
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
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
        
        # eliminando todos los registros
        # delete_query = users.delete()
        
        # eliminando el registro con el id = 1
        # delete_query = users.delete(users.c.id == 1)

        # eliminando todos los registros con la función delete
        # delete_query = delete(users)
        
        # eliminando el registro con el id = 1 con la función delete
        delete_query = delete(users).where(users.c.id == 1)
        
        result = connection.execute(delete_query)
        print(result.rowcount)
        
        select_query = select([users.c.id, users.c.name]).where(users.c.id == 1)
        
        result = connection.execute(select_query)
        user = result.fetchone()
        if user:
            print(user.name)
        else:
            print('No fue posible obtener al usuario!')
        