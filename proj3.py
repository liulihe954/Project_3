#!/usr/bin/env python3 

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import os
# Create a sqlite database housed in memory--no file
engine = create_engine('sqlite:///columns_flights.csv')

metadata=MetaData()
Airlines = Table ('Airlines', metadata,
                Column('AIRLINE_ID', String),
                Column('DISTANCE', Integer),
                Column('ORIGIN_CITY_NAME', String),
                Column('DEST', String)
                )
                metadata.create_all(engine)
Delayed_flights = Table ('Delayed_flights', metadata,
                        Column('FL_DATE', Date)
                        Column('AIRLINE_ID', String), ##this is our foreign key
                        Column('ORIGIN', String),
                        Column('ORIGIN_CITY_NAME', String),
                        Column('DEST', String)
                        )
                        metadata.create_all(engine)
                                                                                                                                                                              ~                               
