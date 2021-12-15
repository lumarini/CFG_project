import requests

class PrepForAPI:  # sorts the data into the correct format to make the API call
    def __init__(self, age_rating, genres, lower_runtime, number_of_results, keywords):
        # options = 15, R18, U, PG, 12A, 12, 18
        self.chosen_age_ratings = age_rating
        self.chosen_genres = genres
        self.chosen_keywords = keywords
        self.chosen_lower_runtime = lower_runtime

        self.age_rating_list = []
        self.all_age_rating = ""
        self.genres_list = []
        self.capitalize_genres = []
        self.number_genres = []
        self.all_genres = ""
        self.keywords_query = ""
        self.ID_list = []
        self.keywords_list = []

    def age_ratings(self):  # Joins all the selected age ratings together in the correct format
        self.chosen_age_ratings = str(self.chosen_age_ratings)
        self.age_rating_list = self.chosen_age_ratings.split(", ")
        self.all_age_rating = "|".join(self.age_rating_list)
        return self.all_age_rating


    def genres(self):  # Changes the genres to the corresponding number and joins them together in the correct format
        self.chosen_genres = str(self.chosen_genres)
        self.genres_list = self.chosen_genres.split(", ")
        for chosen_genre in self.genres_list:
            self.capitalize_genres.append(chosen_genre.title())
        for chosen_genre in self.capitalize_genres:
            if chosen_genre == "Action":
                self.number_genres.append("28")
            elif chosen_genre == "Adventure":
                self.number_genres.append("12")
            elif chosen_genre == "Animation":
                self.number_genres.append("16")
            elif chosen_genre == "Comedy":
                self.number_genres.append("35")
            elif chosen_genre == "Crime":
                self.number_genres.append("80")
            elif chosen_genre == "Documentary":
                self.number_genres.append("99")
            elif chosen_genre == "Drama":
                self.number_genres.append("18")
            elif chosen_genre == "Family":
                self.number_genres.append("10751")
            elif chosen_genre == "Fantasy":
                self.number_genres.append("14")
            elif chosen_genre == "History":
                self.number_genres.append("36")
            elif chosen_genre == "Horror":
                self.number_genres.append("27")
            elif chosen_genre == "Music":
                self.number_genres.append("10402")
            elif chosen_genre == "Mystery":
                self.number_genres.append("9648")
            elif chosen_genre == "Romance":
                self.number_genres.append("10749")
            elif chosen_genre == "Science Fiction":
                self.number_genres.append("878")
            elif chosen_genre == "TV Movie":
                self.number_genres.append("10770")
            elif chosen_genre == "Thriller":
                self.number_genres.append("53")
            elif chosen_genre == "War":
                self.number_genres.append("10752")
            elif chosen_genre == "Western":
                self.number_genres.append("37")
        self.all_genres = "|".join(self.number_genres)
        return self.all_genres

    def lower_runtime(self):  # Returns the chosen lower runtime
        return self.chosen_lower_runtime


    def keywords(self):
        if self.chosen_keywords.data is not None and self.chosen_keywords.data != "":
            self.keywords_list = self.chosen_keywords.data.split(" ")

            # Search up the keyword IDs
            for kw in self.keywords_list:

                parameters = {
                    "api_key": "43c96095652d8dd6ac3f404242b593fe",
                    "query": kw
                }

                url = f"https://api.themoviedb.org/3/search/keyword"
                response = requests.get(url, params=parameters)
                result = response.json()
                try:
                    result = result['results'][0]['id']
                    self.ID_list.append(result)
                except:
                    pass

            self.keywords_query = "|".join([str(x) for x in self.ID_list])
            return self.keywords_query


class CallingAPI(PrepForAPI):
    def __init__(self, age_rating, genres, lower_runtime, number_of_results, keywords):
        super().__init__(age_rating, genres, lower_runtime, number_of_results, keywords)
        self.result = []
        self.films = []

        self.chosen_parameters = {
            "api_key": "43c96095652d8dd6ac3f404242b593fe",
            "sort_by": "popularity.desc",
            "certification_country": "GB",
            "certification.gte": super().age_ratings(),
            "page": 10,
            "with_genres": super().genres(),
            "with_keywords": super().keywords,
            "with_runtime.gte": super().lower_runtime(),
            }

    def api_call(self, parameters):
        # calls the api, if any of the categories are blank, the call will still be made, the results just won't be
        # filtered on the category
        url = f"https://api.themoviedb.org/3/discover/movie"
        response = requests.get(url, params=parameters)
        self.result = response.json()
        self.films = self.result["results"]


class SortingAPI(CallingAPI):
    def __init__(self, age_rating, genres, lower_runtime, number_of_results, keywords):
        super().__init__(age_rating, genres, lower_runtime, number_of_results, keywords)
        self.all_films = []
        self.count = 1

    def sorting_data(self):
        super().api_call(self.chosen_parameters)  # makes the call to the API so the data can then be sorted
        for each_film in self.films:  # gets the relevant data for each film and puts it into a dictionary
            part_poster_path = each_film["poster_path"]
            full_poster_path = f"https://image.tmdb.org/t/p/original/{part_poster_path}"
            current_film = {"Recommendation Option": self.count, "Name": each_film["title"], "ID": each_film["id"],
                            "Description": each_film["overview"], "Poster": full_poster_path}
            self.all_films.append(current_film)
            self.count = self.count + 1

    def displaying_data(self):
        return self.all_films
