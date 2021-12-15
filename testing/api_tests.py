import unittest
from reccomendation.api_calls import PrepForAPI, CallingAPI, SortingAPI


class TestPrepForAPI(unittest.TestCase):
	def test_age_ratings(self):
		expected = "12A|15|PG"
		result = PrepForAPI("12a, 15, pg", "horror", 100).age_ratings()
		self.assertEqual(expected, result)

	def test_genres(self):
		expected = "27|12|14"
		result = PrepForAPI("12a", "horror, adventure, fantasy", 100).genres()
		self.assertEqual(expected, result)


class TestCallingAPI(unittest.TestCase):
	def test_working_api_call(self):
		age_rating = "12A"
		genre = "Horror"
		runtime = 100
		expected = 200

		parameters = {
			"api_key": "43c96095652d8dd6ac3f404242b593fe",
			"sort_by": "popularity.desc",
			"certification_country": "GB",
			"certification": age_rating,
			"with_genres": genre,
			"with_runtime.gte": runtime,
		}

		result = CallingAPI(age_rating, genre, runtime).api_call(parameters)
		self.assertEqual(expected, result)

	def test_missing_key_api_call(self):
		age_rating = "12A"
		genre = "27"
		runtime = 100

		parameters = {
			"api_key": "",
			"sort_by": "popularity.desc",
			"certification_country": "GB",
			"certification": age_rating,
			"with_genres": genre,
			"with_runtime.gte": runtime,
		}

		with self.assertRaises(Exception):
			CallingAPI(age_rating, genre, runtime).api_call(parameters)

	def test_missing_genre_api_call(self):
		age_rating = "12A"
		genre = ""
		runtime = 100

		expected = 200

		parameters = {
			"api_key": "43c96095652d8dd6ac3f404242b593fe",
			"sort_by": "popularity.desc",
			"certification_country": "GB",
			"certification": age_rating,
			"with_genres": genre,
			"with_runtime.gte": runtime,
		}

		result = CallingAPI(age_rating, genre, runtime).api_call(parameters)
		self.assertEqual(expected, result)


class TestSortingAPI(unittest.TestCase):

	def test_sort_of_data(self):
		age_rating = "12A"
		genre = "Horror"
		runtime = 100

		expected = [{'Description': 'A deep sea submersible pilot revisits his past fears in the Mariana Trench, and '
									'accidentally unleashes the seventy foot ancestor of the Great White Shark '
									'believed to be extinct.',
					'ID': 345940,
					'Name': 'The Meg',
					'Poster': 'https://image.tmdb.org/t/p/original//xqECHNvzbDL5I3iiOVUkVPJMSbc.jpg',
					'Recommendation Option': 1}]

		sort = SortingAPI(age_rating, genre, runtime)
		sort.films = [{'adult': False, 'backdrop_path': '/rH79sB6Nkx4cMW3JzsUy7wK0rhX.jpg', 'genre_ids': [28, 878, 27],
						'id': 345940, 'original_language': 'en', 'original_title': 'The Meg', 'overview': 'A deep sea '
						'submersible pilot revisits his past fears in the Mariana Trench, and accidentally unleashes the '
						'seventy foot ancestor of the Great White Shark believed to be extinct.', 'popularity': 72.476,
						'poster_path': '/xqECHNvzbDL5I3iiOVUkVPJMSbc.jpg', 'release_date': '2018-08-09', 'title':
						'The Meg', 'video': False, 'vote_average': 6.2, 'vote_count': 5577}]

		result = sort.sorting_data()
		self.assertEqual(expected, result)
