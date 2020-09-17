import requests
import math
import random
from peerflix import peerflix


class Search:
    def __init__(self, genre, rating):
        self.genre = genre
        self.rating = rating
        self.pageLimit = 50

    def handleMovieParams(self):
        url = f"https://yts.mx/api/v2/list_movies.json?genre={self.genre}&minimum_rating={self.rating}&limit={self.pageLimit}"
        self.requestMovieData(url)

    def requestMovieData(self, url):
        response = requests.get(url).json()
        amountMovies = response["data"]["movie_count"]
        totalPages = math.ceil(amountMovies / self.pageLimit)
        
        randomPage = requests.get(url + f"&page={str(random.randint(1, totalPages))}").json()
        randomMovie = randomPage["data"]["movies"][random.randint(0, 49)]
        
        print("Found a random movie!")
        print(f"Title: {randomMovie['title']}")
        for q in randomMovie["torrents"]:
            print(f"Quality: {q['quality']} with {q['seeds']} seeds")

        highQuality = randomMovie["torrents"][1]
        if not highQuality:
            self.startMovieStreaming(randomMovie["torrents"][0]["url"], "mpchc", True)
        else:
            self.startMovieStreaming(randomMovie["torrents"][1]["url"], "mpchc", True)

    def startMovieStreaming(self, url, player, remove):
        peerflix(url, player, remove)
        


