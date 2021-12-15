# Imports:
import mysql.connector
from db_config import HOST, USER, PASSWORD, KEY


# Constants:
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


def read_db(sql_query, db_name=DATABASE, fetchall=True):
    """function to read and fetch info from db
    -- only READS from DB --
    do not use to insert/delete/update"""
    try:
        conn = db_connection(DATABASE)
        cursor = conn.cursor()
        print(f"Successfully connected to DB {db_name}")
    except Exception:
        raise ConnectionRefusedError("Failed to connect to DB")
    else:
        cursor.execute(sql_query)
        if fetchall == True:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        cursor.close()
    finally:
        if conn:
            conn.close()
            print("DB connection is closed")
    return result


# Functionalities to DB:

#  1 --- REGISTER USER

def register_new_user(user, password):

    """Function to register new user onto DB"""

    INSERT_USER = f"""INSERT INTO users (username, password)
        VALUES ('{user}', AES_ENCRYPT('{password}','{KEY}'));"""
    try:
        query_db(INSERT_USER)
    except Exception:
        raise ConnectionRefusedError("Failed to insert user into DB.")
    else:
        print(f"User {user} successfully added.")
    return user


#  2 --- LOGIN
def authenticate_user(user, password_inserted):

    """Function to authenticate user that was already registered onto DB"""

    query = f"""SELECT AES_DECRYPT(password, '{KEY}')
                FROM users
                WHERE username = '{user}';"""
    try:
        result = read_db(query, fetchall=False)
    except Exception:
        raise ConnectionRefusedError("User not found on DB.")
    else:
        password_decrypted = result[0].decode()
        if password_inserted == password_decrypted:
            return True
        else:
            print("Username and password do not match.")
            return False


def find_id(user):

    """Function to find user_id"""

    query = f"""SELECT user_id
                FROM users
                WHERE username = '{user}';"""
    try:
        result = read_db(query, fetchall=False)
    except Exception:
        raise ConnectionRefusedError("User not found on DB.")
    else:
        return result[0]


def lookup_username(username):

    """Function to see if username exists"""
    query = f"""SELECT user_id
                FROM users
                WHERE username = '{username}';"""
    try:
        result = read_db(query, fetchall=False)
    except Exception:
        raise ConnectionRefusedError("User not found on DB.")
    else:
        if not result:
            return True
        else:
            return False
        # return result[0]


lookup_username("hello")
#  3 --- FETCH ALL 'MOVIES ALREADY WATCHED' FROM CURRENT USER LOGGED IN



def get_movies_watched(current_user):

    """Function to fetch movies already registered by user as "already watched", so
    it does not shows on the recommendation list again. Should be used to be compared against
    the list of recommendations before showcasing it to the user -- if user has marked the movie
    as already watched, do not show the recommendation again"""

    list_of_movies_watched = []
    movie_ids = []
    query = f"""SELECT m.movie_id, m.movie_name, m.movie_detail, m.movie_poster_path
                from users u, movies m, movies_watched mw
                where mw.user_id = u.user_id AND mw.movie_id = m.movie_id 
                AND u.user_id = {current_user};"""
    try:
        result = read_db(query, fetchall=True)
    except Exception:
        raise ConnectionRefusedError("Not found movies already watched for this user.")
    else:
        if not result:
            return False
        else:
            all_films = []
            for line in result:
                current_film = {"Name": line[1],
                                "ID": line[0],
                                "Description": line[2],
                                "Poster": line[3]}
                all_films.append(current_film)
            return all_films


# print(get_movies_watched(1))
#  4 --- ADD NEW MOVIE ON 'MOVIES ALREADY WATCHED' FROM CURRENT USER LOGGED IN

def insert_movie_watched(current_user_id, movie_id, movie_name, movie_detail, movie_poster_path):

    """Query A - inserts movie to the list of movies (if not already there -- insert ignore / upsert).
       Query B - inserts an entry stating user id and movie id (join for tables users and movies)
       creating a many-to-many relationship. Each line is a different movie marked as already watched
       by a specific user. It does not duplicate a record already on the database (insert ignore / upsert)"""

    query_a = f"""INSERT IGNORE INTO movies (movie_id, movie_name, movie_detail, movie_poster_path)
                VALUES ({movie_id}, '{movie_name}', '{movie_detail}', '{movie_poster_path}');"""
    try:
        query_db(query_a)   # Insert movie into movies table if not already there
    except Exception:
        raise ConnectionRefusedError("Could not add this movie to list of movies.")

    query_b = f"""INSERT IGNORE INTO movies_watched (user_id, movie_id)
                VALUES ({current_user_id}, {movie_id});"""
    try:
        query_db(query_b)   # add movie to attached to user's list of watched movies
    except Exception:
        raise ConnectionRefusedError("Could not add this movie to list of movies already watched")
    else:
        print(f" Movie {movie_name} successfully added as already watched by user {current_user_id}.")
        return movie_id


"""STEPS for implementing DB connection: """
"""
1 - Run the SQL codes to create the DB

2 - Adjust values on the file db_config.py to reflect your own machine. Usually, the values for HOST = "localhost"
and USER = "root", and what changes is the password; 

3- After creating the DB, try running the line of code below to create the user Nina:
"""
# register_new_user('Nina', 'nina@email', 'password')

""" 4- After that, please try to run the code below to authenticate the user Nina, given the username and password,
which should return true"""

# print(authenticate_user('Nina', 'password'))


"""
5- After creating the user, let's try to add a movie that was already watched by this user Nina
"""
# insert_movie_watched(1, 1, "The Lion King", "Comedy, cartoon")

"""
5- Lastly, let's fetch the movies already watched by user by user_id:
"""
# print(get_movies_watched(1))

"""
Comments:
I am not sure if there are need for the email field on the user details, but it can be dropped if needed.

Also, on the movies table, the "movie detail" can also be dropped, I believe only movie id or the movie number
that is used as reference on TheMovieDB suffice for the purpose of the code.

The encryption is being done in SQL, as it was impossible to convert the password into binary code and then append
it to MySQL, because the encrypted string usually has slashes and apostrophes, and any other special characteres that
cannot be unscaped, so it creates problems if you encrypt in python and then push it to the DB, it just creat too many
errors, so I am using the standard AES encryption pattern on MySQL database
"""