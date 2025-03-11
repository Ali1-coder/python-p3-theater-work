from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Audition(Base):
    __tablename__='auditions'

    id=Column(Integer,primary_key=True)
    actor=Column(String,nullable=False)
    location=Column(String,nullable=False)
    phone=Column(Integer,nullable=False)
    hired=Column(Boolean,default=False)
    role_id=Column(Integer,ForeignKey('roles.id'),nullable=False)

    def call_back(self,session):
        self.hired=True
        session.commit()

class Role(Base):
    __tablename__='roles'
    
    id=Column(Integer,primary_key=True)
    character_name=Column(String,nullable=False)

    auditions=relationship('Audition',backref='role',lazy=True)

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        leader= [l for l in self.auditions if l.hired]
        return leader[0] if leader else 'no actor has been hired for this role'

    def understudy(self):
        leader= [l for l in self.auditions if l.hired]
        return leader[1] if len(leader) > 1 else 'no actor has been hired for understudy for this role'



if __name__ == '__main__':
    engine=create_engine('sqlite:///moringa_auditions.db')
    Base.metadata.create_all(engine)

    # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()

    