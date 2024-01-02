from sql_connection import get_sql_connection

def get_all_products(connection) -> list:
    cursor = connection.cursor()

    query = """
            SELECT p.product_id, p.name, u.uom_name, p.price_per_unit
                FROM products AS p 
                INNER JOIN uom AS u 
                ON p.uom_id = u.uom_id
                ORDER BY p.product_id ASC;
            """
    cursor.execute(query)

    response = []

    for (product_id, name, uom, price_per_unit) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_name': uom,
                'price_per_unit': price_per_unit
            }
        )

    return response

def insert_new_product(connection, product) -> str:
    cursor = connection.cursor()
    query = """INSERT INTO products (name, uom_id, price_per_unit) 
                    VALUES (%s, %s, %s);
            """
    data = (product['name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product) -> str:
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = " + str(product['product_id']) + ";"
    cursor.execute(query)
    connection.commit()
    return 'Deleted'

if __name__ == '__main__':
    connection = get_sql_connection()
    while True:
        print("Option 1: view products\nOption 2: new product\nOption 3: delete product\nOption 0: Exit")
        option = int(input("Option -> "))
        if option == 1:
            print(get_all_products(connection))
        elif option == 2:
            product = {}
            product['name'] = input('Product name -> ')
            product['uom_id'] = int(input('Product uom_id -> '))
            product['price_per_unit'] = float(input('Product price_per_unit -> '))
            print(insert_new_product(connection, product))
        elif option == 3:
            id = input('Product_id to delete -> ')
            product = {'product_id': id}
            print(delete_product(connection, product))
        else:
            break
    connection.close()
