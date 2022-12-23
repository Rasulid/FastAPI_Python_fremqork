import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engen = sqlalchemy.create_engine("sqlite:///sqlite.db")