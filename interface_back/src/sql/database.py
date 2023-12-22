import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
import pyodbc


connection_string = (f'DRIVER={config.DRIVER};'
                     f'SERVER={config.DB_HOST};'
                     f'DATABASE={config.DB_NAME};'
                     f'UID={config.DB_USERNAME};'
                     f'PWD={config.DB_PASSWORD};'
                     f'PORT={config.DB_PORT}')

# connection_string = (f'DRIVER={config.DRIVER};'
#                      f'SERVER={config.DB_HOST};'
#                      'Trusted_Connection=yes;'
#                      f'DATABASE={config.DB_NAME};')


conn = pyodbc.connect(connection_string)

# connection_url = sqlalchemy.engine.URL.create(
#     drivername=config.DRIVER,
#     username=config.DB_USERNAME,
#     password=config.DB_PASSWORD,
#     host=config.DB_HOST,
#     database=config.DB_NAME,
#     port=config.DB_PORT
# )

# engine = create_engine(
#     f"mssql+pyodbc://{config.DB_HOST}/{config.DB_NAME}?trusted_connection=yes&driver={config.DRIVER}",
#     echo=True)

# engine = create_engine(connection_url, echo=True)
# crud_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# connection_url = create_engine(
#     f"mssql+pyodbc://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}?driver={config.DRIVER}"
# )
