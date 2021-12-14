class Authenticate:

	def __init__(self, age_rating, genres, lower_runtime):
		self.chosen_age_ratings = age_rating
		self.chosen_genres = genres
		# in mins
		self.chosen_lower_runtime = lower_runtime
		# in mins
		self.age_rating_list = []
		self.upper_age_ratings = []
		self.all_age_rating = ""
		self.genres_list = []
		self.capitalize_genres = []
		self.number_genres = []
		self.all_genres = ""
		self.genre_mes = ""
		self.age_rating_mes = ""
		self.runtime_mes = "The runtime must be a number over 0"

	def age_ratings(self):  # Joins all the selected age ratings together in the correct format
		self.chosen_age_ratings = str(self.chosen_age_ratings)
		self.age_rating_list = self.chosen_age_ratings.split(", ")
		for chosen_age_rating in self.age_rating_list:
			self.upper_age_ratings.append(chosen_age_rating.upper())
		available_age_ratings = ["15", "R18", "U", "PG", "12A", "12", "18"]

		incorrect_age_rating = []
		for chosen_age_rating in self.upper_age_ratings:
			if chosen_age_rating not in available_age_ratings:
				incorrect_age_rating.append(chosen_age_rating)
		if not incorrect_age_rating:
			return True
		elif len(incorrect_age_rating) == 1:
			self.age_rating_mes = f"{incorrect_age_rating[0]} is not an available age rating"
			return False
		else:
			age_ratings = ", ".join(incorrect_age_rating)
			self.age_rating_mes = f"{age_ratings} are not available age ratings"
			return False

	def age_rating_message(self):
		return self.age_rating_mes

	def genres(self):  # Changes the genres to the corresponding number and joins them together in the correct format
		self.chosen_genres = str(self.chosen_genres)
		self.genres_list = self.chosen_genres.split(", ")
		for chosen_genre in self.genres_list:
			self.capitalize_genres.append(chosen_genre.title())
		available_genres = ["Action", "Adventure", "Animation", "Comedy" "Crime", "Documentary", "Drama", "Family",
		                    "Fantasy", "History", "Horror", "Music", "Romance", "Science Fiction", "TV Movie",
		                    "Thriller", "War", "Western"]

		incorrect_genre = []
		for chosen_genre in self.capitalize_genres:
			if chosen_genre not in available_genres:
				incorrect_genre.append(chosen_genre)

		if not incorrect_genre:
			return True
		elif len(incorrect_genre) == 1:
			self.genre_mes = f"{incorrect_genre[0]} is not an available genre"
			return False
		else:
			genres = ", ".join(incorrect_genre)
			self.genre_mes = f"{genres} are not available genres"
			return False

	def genre_message(self):
		return self.genre_mes

	def lower_runtime(self):  # Returns the chosen lower runtime
		if int(self.chosen_lower_runtime) > 0:
			return True
		else:
			return False

	def runtime_message(self):
		return self.runtime_mes

