import databases
import sqlalchemy

metadata = sqlalchemy.MetaData() # помогает работать с sqlalchemy core - ядро
database = databases.Database("sqlite:///sqlite.db")  # позволяет управлять ассинхрона базой данных
engin = sqlalchemy.create_engine("sqlite:///sqlite.db")