from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1976633854@localhost:3307/baseprueba"
engine= create_engine(SQLALCHEMY_DATABASE_URL)

# Creamos una sesión que nos permitirá trabajar con la base de datos
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Declaramos la base que usaremos para definir las tablas en la base de datos
Base = declarative_base()