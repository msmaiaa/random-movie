import requests

class Search:
    def __init__(self, genre, rating):
        self.genre = genre
        self.rating = rating

    def searchMovies(self):
        url = f"https://yts.mx/api/v2/list_movies.json?genre={self.genre}&minimum_rating={self.rating}&limit=20"
        query = requests.get(url).json()
        amountMovies = query["data"]["movie_count"]
        pageLimit = 20
        for i in range (1, amountMovies / pageLimit):
            


