import requests


class PrepForAPI:  # sorts the data into the correct format to make the API call
    def __init__(self):
        # options = 15, R18, U, PG, 12A, 12, 18
        self.chosen_age_ratings = ["15", "12"]  # needs replacing with input from front end
        self.chosen_genres = ["action", "comedy"]  # needs replacing with input from front end
        # in mins
        self.chosen_lower_runtime = 120  # needs replacing with input from front end
        # in mins
        self.chosen_upper_runtime = 120  # needs replacing with input from front end
        # from 0 to 10
        self.chosen_rating = 7.4  # needs replacing with input from front end
        self.all_age_rating = ""
        self.capitalize_genres = []
        self.number_genres = []
        self.all_genres = ""

    def age_ratings(self):  # Joins all the selected age ratings together in the correct format
        self.all_age_rating = "|".join(self.chosen_age_ratings)
        return self.all_age_rating

    def genres(self):  # Changes the genres to the corresponding number and joins them together in the correct format
        for chosen_genre in self.chosen_genres:
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

    def upper_runtime(self):  # Returns the chosen upper runtime
        return self.chosen_upper_runtime

    def rating(self):  # Returns the rating
        return self.chosen_rating


class CallingAPI(PrepForAPI):
    def __init__(self):
        super().__init__()
        self.result = []
        self.films = []

    def api_call(self):
        # calls the api, if any of the categories are blank, the call will still be made, the results just won't be
        # filtered on the category
        url = f"https://api.themoviedb.org/3/discover/movie?api_key=43c96095652d8dd6ac3f404242b593fe" \
            f"&sort_by=popularity.desc&certification_country=GB&certification={super().age_ratings()}" \
            f"&with_genres={super().genres()}&with_runtime.gte={super().lower_runtime()}" \
            f"&with_runtime.lte={super().upper_runtime()}&vote_average.gte={super().rating()}"
        response = requests.get(url)
        self.result = response.json()
        self.films = self.result["results"]


class SortingAPI(CallingAPI):
    def __init__(self):
        super().__init__()
        self.all_films = []
        self.count = 1

    def sorting_data(self):
        super().api_call()  # makes the call to the API so the data can then be sorted
        for each_film in self.films:  # gets the relevant data for each film and puts it into a dictionary
            part_poster_path = each_film["poster_path"]
            full_poster_path = f"https://image.tmdb.org/t/p/original/{part_poster_path}"
            current_film = {"Recommendation Option": self.count, "Name": each_film["title"], "ID": each_film["id"],
                            "Description": each_film["overview"], "Poster": full_poster_path}
            self.all_films.append(current_film)
            self.count = self.count + 1
        for film in self.all_films:
            # this is just to show what data is being selected and won't stay here, the relevant parts will need to be
            # displayed to the user but let me know if there's anything missing
            print(film)


SortingAPI().sorting_data()
