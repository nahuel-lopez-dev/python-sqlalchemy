from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

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
    
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    user_id = Column(ForeignKey('users.id'))  
    created_at = Column(DateTime(), default=datetime.now()) 
    
    def __str__(self):
        return self.title 
        
# un usuario puede tener múltiples cursos y un curso le pertenece a un usuario    
Session = sessionmaker(engine)   
session = Session() 

if __name__ == '__main__':
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    user1 = User(username='user1', email='user1@example.com')
    user2 = User(username='user2', email='user2@example.com')    
    
    session.add(user1)
    session.add(user2)
    
    session.commit()

    course1 = Course(title='Curso profesional de Base de Datos', user_id=user1.id)
    session.add(course1)
    session.commit()
    