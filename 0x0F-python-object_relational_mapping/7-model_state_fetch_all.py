#!/usr/bin/python3
""" Link the class to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmamker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}localhost:3306/{}'
                           .format(sys.rgv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
