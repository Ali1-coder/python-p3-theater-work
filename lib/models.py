from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Audition(Base):
    __tablename__='auditions'

    id=Column(Integer,primary_key=True)
    actor=Column(String,nullable=False)
    location=Column(String,nullable=False)
    phone=Column(Integer,nullable=False)
    hired=Column(Boolean,nullable=False)
    role_id=Column(Integer,ForeignKey('roles.id'),nullable=False)

class Role(Base):
    __tablename__='roles'
    
    id=Column(Integer,primary_key=True)
    character_name=Column(String,nullable=False)

    auditions=relationship('Audition',backref='role',lazy=True)


if __name__ == '__main__':
    engine=create_engine('sqlite:///moringa_auditions.db')
    Base.metadata.create_all(engine)

    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()