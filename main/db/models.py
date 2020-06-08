from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Office(Base):
    __tablename__ = "office"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "people_working": [person.to_dict_no_office() for person in self.people_working]
        }


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    office_id = Column(Integer, ForeignKey('office.id'), nullable=True)
    office = relationship(Office, backref=backref('people_working', uselist=True))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "office_id": self.office_id,
            "office": self.office.name if isinstance(self.office, Office) else None
        }

    def to_dict_no_office(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
        }
