class Authenticate:

	def __init__(self, age_rating, genres, lower_runtime, upper_runtime):
		self.chosen_age_ratings = age_rating
		self.chosen_genres = genres
		# in mins
		self.lower_chosen_runtime = lower_runtime
		# in mins
		self.upper_chosen_runtime = upper_runtime
		self.age_rating_list = []
		self.upper_age_ratings = []
		self.all_age_rating = ""
		self.genres_list = []
		self.capitalize_genres = []
		self.number_genres = []
		self.all_genres = ""
		self.genre_mes = ""
		self.age_rating_mes = ""
		self.lower_runtime_mes = ""
		self.upper_runtime_mes = ""

	def age_ratings(self):  # Joins all the selected age ratings together in the correct format
		if not self.chosen_age_ratings:
			return True
		try:
			self.chosen_age_ratings = str(self.chosen_age_ratings)
		except:
			self.age_rating_mes = f"{self.chosen_age_ratings} is not an available age rating"
			return False
		else:
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
		try:
			self.chosen_genres = str(self.chosen_genres)
		except:
			self.genre_mes = f"{self.chosen_genres[0]} is not an available genre"
			return False
		else:
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
		if not self.lower_chosen_runtime or self.lower_chosen_runtime == "":
			return True
		try:
			int(self.lower_chosen_runtime)
		except:
			self.lower_runtime_mes = "The minimum runtime must be a number over 0"
			return False
		else:
			if int(self.lower_chosen_runtime) >= 0:
				return True
			else:
				self.lower_runtime_mes = "The minimum runtime must be a number over 0"
				return False

	def lower_runtime_message(self):
		return self.lower_runtime_mes

	def upper_runtime(self):  # Returns the chosen lower runtime
		if not self.upper_chosen_runtime or self.upper_chosen_runtime == "":
			return True
		try:
			int(self.upper_chosen_runtime)
		except:
			self.upper_runtime_mes = "The maximum runtime must be a number over 0"
			return False
		else:
			if int(self.upper_chosen_runtime) > 0:
				if self.lower_chosen_runtime:
					if self.upper_chosen_runtime > self.lower_chosen_runtime:
						return True
					else:
						self.upper_runtime_mes = "The maximum runtime must be larger than the minimum runtime"
						return False
				else:
					return True
			else:
				self.upper_runtime_mes = "The maximum runtime must be a number over 0"
				return False

	def upper_runtime_message(self):
		return self.upper_runtime_mes
