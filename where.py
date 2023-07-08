
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

from sqlalchemy import select

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

if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    with engine.connect() as connection:
        # abriendo users.json
        with open('users.json') as file:            
            # Cargando la tabla con los usuarios
            connection.execute(users.insert(), json.load(file))
        
        # SELECT * FROM users WHERE country == 'Frances;
        # select_query = users.select(users.c.country == 'France')
        
        # SELECT id, email, name, FROM users WHERE country == 'France
        select_query = select([
            users.c.id,
            users.c.email,
            users.c.name
        ]).where(
            users.c.country == 'France'
        )
        
        print(select_query)
        
        result = connection.execute(select_query) # ResultProxy
        
        for user in result.fetchall():
            print(user.email) # objetos RowProxy
            
            