from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

#Nome do servidor e Base de dados
SERVER_NAME = r"GHOST_RIDER\SQLEXPRESS"
DATABASE_NAME = "BALATRO"

#String de conexão com o banco de dados
DATABASE_URL = f"mssql+pyodbc://{SERVER_NAME}/{DATABASE_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()