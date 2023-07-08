
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime

from sqlalchemy import select
from sqlalchemy import and_, or_, not_

from sqlalchemy import desc, asc

engine = create_engine('postgresql://postgres:@localhost/sqlalchemy')
metadata = MetaData()

# users
users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('username', String(), index=True, nullable=False),
    Column('email', String(),nullable=False),
    Column('created_at', DateTime(), default=datetime.now),
)

if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    with engine.connect() as connection:
        # abriendo users.json
        with open('users.json') as file:            
            # Cargando la tabla con los usuarios
            connection.execute(users.insert(), json.load(file))
        
        # listar en consola de forma desc. el nombre de los primeros 10 usuarios
        # cuyo género sea femenino y posean por país Alemania o España.
        
        # SELECT id, email, name, FROM users WHERE country == 'France
        select_query = select([
            users.c.name
        ]).where(
            and_(
                users.c.gender == 'female',
                or_(
                    users.c.country == 'Germany',
                    users.c.country == 'Spain'
                )
            )
        ).order_by(
            desc(users.c.name)
        ).limit(10)
        
        response = connection.execute(select_query) # ResultProxy
        
        for user in response.fetchall():
            print(user.name) # objetos RowProxy
            
            