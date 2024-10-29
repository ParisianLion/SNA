from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Association table for many-to-many relationship
association_table = Table('association', Base.metadata,
    Column('contact_id', Integer, ForeignKey('contacts.id')),
    Column('related_contact_id', Integer, ForeignKey('contacts.id'))
)

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    relationships = relationship(
        'Contact',
        secondary=association_table,
        primaryjoin=id==association_table.c.contact_id,
        secondaryjoin=id==association_table.c.related_contact_id,
        backref='related_to'
    )

class Interaction(Base):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(String)
    contact = relationship('Contact', backref='interactions')
