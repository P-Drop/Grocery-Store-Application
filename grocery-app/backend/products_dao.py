import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

cnx = mysql.connector.connect(
                            user = os.getenv("DB_USER"), password= os.getenv('DB_PW'),
                            host = os.getenv('DB_HOST'),
                            database = os.getenv('DB_NAME')
                            )
cursor = cnx.cursor()

query = "SELECT * FROM grocery_store.products"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)

cnx.close()