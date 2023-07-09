
import json
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, 
                        Column, 
                        Integer, 
                        String, 
                        DateTime, 
                        Float, 
                        ForeignKey)

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import and_, or_, not_

from sqlalchemy import desc, asc

engine = create_engine('postgresql://postgres:@localhost/sqlalchemy')
metadata = MetaData()


orders = Table(
    'orders',
    metadata,
    Column('id', Integer(), primary_key=True)
)

products = Table(
    'products',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('title', String()),
    Column('price', Float(5,2)),
    Column('order_id', ForeignKey('orders.id'))
)

if __name__ == '__main__':
    
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
    with engine.connect() as connection:
        
        # Orden
        insert_query = orders.insert()
        connection.execute(insert_query)

        # Productos
        # Iphone
        insert_query = products.insert().values(
            title='Iphone',
            price=500.50,
            order_id=1
        )
        connection.execute(insert_query)
        
        # IPad
        insert_query = products.insert().values(
            title='IPad',
            price=800.00,
            order_id=1
        )
        connection.execute(insert_query)
        
        # Macbook
        insert_query = products.insert().values(
            title='Macbook',
            price=2000.00,
            order_id=1
        )
        connection.execute(insert_query)
        
        