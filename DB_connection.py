###Imports:
import mysql.connector
from db_config import HOST, USER, PASSWORD


###Constants:
DATABASE = 'movie_recommendations'
TABLE_USERS = "users"
TABLE_MOVIES = "movies"
TABLE_MOVIES_WATCHED = "movies_watched"


def db_connection(db_name):
    """create conn with DB"""
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return conn


def query_db(sql_query, db_name=DATABASE):
    """function to add/delete/update data on table"""
    try:
        conn = db_connection(DATABASE)
        cursor = conn.cursor()
        print(f"Successfully connected to DB {db_name}")

    except Exception:
        raise ConnectionRefusedError("Failed to connect to DB")

    else:
        cursor.execute(sql_query)
        conn.commit()
        cursor.close()

    finally:
        if conn:
            conn.close()
            print("DB connection is closed")



def read_db(sql_query, db_name=DATABASE):
    """function to read and fetch info from db -- READ ONLY -- not use to insert/delete or update"""
    try:
        conn = db_connection(DATABASE)
        cursor = conn.cursor()
        print(f"Successfully connected to DB {db_name}")

    except Exception:
        raise ConnectionRefusedError("Failed to connect to DB")

    else:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        # for line in result:
        #     print(line)
        cursor.close()

    finally:
        if conn:
            conn.close()
            print("DB connection is closed")

    return result



###Functionalities to implement on DB:

###  1 --- REGISTER USER

def register_new_user(user, email, password):
    INSERT_USER = f"""INSERT INTO users (username, email, password)
        VALUES ('{user}', '{email}', '{password}');"""
    query_db(INSERT_USER)
    print(f"User {user} successfully added.")
    return user


###  2 --- LOGIN



###  3 --- FETCH ALL 'MOVIES ALREADY WATCHED' FROM CURRENT USER LOGGED IN
def get_movies_watched(current_user):
    list_of_movies_watched = []
    movie_ids = []
    query = f"""SELECT u.user_id, u.username, m.movie_id, m.movie_name
                from users u, movies m, movies_watched mw
                where mw.user_id = u.user_id AND mw.movie_id = m.movie_id 
                AND u.user_id = {current_user};"""
    result = read_db(query)
    for line in result:
         list_of_movies_watched.append(line)
         movie_ids.append(line[2])
    print(list_of_movies_watched)
    print(movie_ids)
    return list_of_movies_watched


###  4 --- ADD NEW MOVIE ON 'MOVIES ALREADY WATCHED' FROM CURRENT USER LOGGED IN

def insert_movie_watched(current_user, movie):
    query_a = f"""INSERT IGNORE INTO movies (movie_id, movie_name, movie_detail)
                VALUES (002, 'Monsters, INC.', 'Comedy, Cartoon');"""
    query_db(query_a)

    query_b = f"""INSERT IGNORE INTO movies_watched (user_id, movie_id)
                VALUES ({current_user}, {movie});"""
    query_db(query_b)
    print(f" Movie {movie} successfully added as already watched by user {current_user}.")
    return movie


# SELECT_ALL = f"""SELECT * FROM {TABLE_MOVIES}"""
# read_db(SELECT_ALL)

insert_movie_watched(3, 1)
get_movies_watched(3)