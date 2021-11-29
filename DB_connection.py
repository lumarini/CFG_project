import mysql.connector
from DB_config import USER, PASSWORD, HOST



def DB_connection(db_name):
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return conn



def get_all_users():
    try:
        db_name = 'movie_recommendations'
        db_connection = DB_connection(db_name)
        cursor = db_connection.cursor()
        print(f"Successfully connected to DB {db_name}")
        table_name = "users"
        query = f"""SELECT * FROM {table_name}"""
        cursor.execute(query)
        result = cursor.fetchall()
        for r in result:
            print(r)
        cursor.close()

    except Exception:
        raise ConnectionRefusedError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")



def add_new_user(user, email, password):
    try:
        db_name = 'movie_recommendations'
        db_connection = DB_connection(db_name)
        if db_connection:
            print(f"Successfully connected to DB {db_name}")

        cursor = db_connection.cursor()

        query = f"""
        INSERT INTO users (username, email, password)
        VALUES 
        ('{user}', '{email}', '{password}');
        """
        cursor.execute(query)
        db_connection.commit()
        print("New user added to DB.")
        cursor.close()

    except Exception:
        raise ConnectionRefusedError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


add_new_user('another_user', 'email@domain', 'my_password')
get_all_users()
