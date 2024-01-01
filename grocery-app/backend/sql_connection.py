import os, mysql.connector
from dotenv import load_dotenv

load_dotenv()

__cnx = None

def get_sql_connection() -> mysql.connector.connection:
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
                                user = os.getenv("DB_USER"), password= os.getenv('DB_PW'),
                                host = os.getenv('DB_HOST'),
                                database = os.getenv('DB_NAME')
                                )
    return __cnx