
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
        
        select_query = users.select()
        # print(select_query)
        
        result = connection.execute(select_query) # ResulProxy
        
        for user in result.fetchall():
            print(user)
            
            
    

