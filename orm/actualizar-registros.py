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
    
    # obteniendo el único registro de la consulta para luego modificarlo
    # 1) una forma
    user = session.query(User).filter(User.id == 1).first()
    # accediendo a los atributos y asignando nuevos valores
    user.username = 'Nuevo username'
    user.email = 'nuevoemail@example.com'
    # agregando los cambios al stack
    session.add(user)
    # confirmando los cambios
    session.commit()
    # print(user)
    
    # 2) otra forma mediante la actualización en la consulta
    session.query(User).filter(
        User.id == 2
    ).update(
        {
            User.username: 'Nuevo username2',
            User.email: 'nuevoemail2@example.com'
        }
    )
    
    session.commit()
    
