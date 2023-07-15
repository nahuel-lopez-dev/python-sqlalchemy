from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('postgresql://postgres:@localhost/pythonpg')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    
    def __str__(self):
        return self.username
    
Session = sessionmaker(engine)   
session = Session() 

if __name__ == '__main__':
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    user1 = User(username='User1', email='user1@example.com')
    user2 = User(username='User2', email='user2@example.com')
    user3 = User(username='User3', email='user3@example.com')
    
    # añadiendo los cambios al stack 
    session.add(user1)
    session.add(user2)
    session.add(user3)
    
    # ejecutando y persistiendo los cambios
    session.commit()
    
    # obteniendo registros: SELECT * FROM users;
    # users = session.query(User).all() # retorna una lista iterable
    
    # obteniendo registros en base a una o varias condiciones
    # SELECT * FROM users WHERE id >= 2 and username = 'User3'
    # users = session.query(User).filter(
    #     User.id >= 2
    # ).filter(
    #     User.username == 'User3'
    # )
    
    # Importante
    # Clase --> Instancias de dicha clase
    # Argumentos --> Tuplas
    
    # obteniendo tuplas
    # users = session.query(User.id, User.username, User.email).filter(
    #     User.id >= 2
    # )
    
    users = session.query(User).filter(
        User.id >= 2
    )
    
    for user in users:
        print(user.created_at)
    
    
