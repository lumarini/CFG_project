from db_connection import register_new_user, find_id, lookup_username, get_movies_watched, insert_movie_watched, check_movies_watched
import unittest
from unittest.mock import patch

class TestingDatabaseFunctions(unittest.TestCase):

    @patch("db_connection.query_db")
    def test_register_new_user(self, mock_query_db):
        register_new_user("Username", "Password1")
        
        mock_query_db.assert_called_with("INSERT INTO users (username, password)\n        VALUES ('Username', AES_ENCRYPT('Password1','thisisaverylongstringtobeusedasencryptionkey'));")


    @patch("db_connection.read_db")
    def test_find_id(self, mock_read_db):
        mock_read_db.return_value = [1, 2, 3]
        result = find_id("Username")

        mock_read_db.assert_called_with("SELECT user_id\n                FROM users\n                WHERE username = 'Username';", fetchall=False)

        self.assertEqual(result, 1)


    @patch("db_connection.read_db")
    def test_lookup_username(self, mock_read_db):
        lookup_username("Username")
        mock_read_db.assert_called_with("SELECT user_id\n                FROM users\n                WHERE username = 'Username';", fetchall=False)




    @patch("db_connection.read_db")
    def test_get_movies_watched(self, mock_read_db):

        get_movies_watched("Username")
        mock_read_db.assert_called_with('SELECT m.movie_id, m.movie_name, m.movie_detail, m.movie_poster_path\n                from users u, movies m, movies_watchlist mw\n                where mw.user_id = u.user_id AND mw.movie_id = m.movie_id \n                AND u.user_id = Username;', fetchall=True)
    
    

    @patch("db_connection.read_db")
    def test_check_movies_watched(self, mock_read_db):
        mock_read_db.return_value = "1"
        movie_ids = check_movies_watched("123")
        mock_read_db.assert_called_with('SELECT mw.movie_id from movies_watchlist mw\n                where mw.user_id = 123;', fetchall=True)
        self.assertEqual(movie_ids, ["1"])


    @patch("db_connection.query_db")
    def test_insert_movie_watched_a(self, mock_query_db):
        mock_query_db.return_value = "123"
        movie_id = insert_movie_watched("1", "123", "Finding Nemo", "This is a movie about a fish", "Movie poster path")

        mock_query_db.assert_called_with('INSERT IGNORE INTO movies_watchlist (user_id, movie_id)\n                VALUES (1, 123);')
        self.assertEqual(movie_id, "123")

        


if __name__ == '__main__':
    unittest.main()










