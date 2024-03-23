#!/usr/bin/python3
"""A script that prints the State object with the name passed as argument"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # set up connection to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # query the database
    state = session.query(State).filter(State.name == argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
