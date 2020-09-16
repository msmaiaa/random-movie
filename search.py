import requests
import math
import random
from peerflix import peerflix


class Search:
    def __init__(self, genre, rating):
        self.genre = genre
        self.rating = rating
        self.pageLimit = 50

    def searchMovies(self):
        url = f"https://yts.mx/api/v2/list_movies.json?genre={self.genre}&minimum_rating={self.rating}&limit={self.pageLimit}"
        response = requests.get(url).json()
        amountMovies = response["data"]["movie_count"]
        totalPages = math.ceil(amountMovies / self.pageLimit)
        
        randomPage = requests.get(url + f"&page={str(random.randint(1, totalPages))}").json()
        randomMovie = randomPage["data"]["movies"][random.randint(0, 49)]
        
        print("Found a random movie!")
        print(f"Title: {randomMovie['title']}")
        for q in randomMovie["torrents"]:
            print(f"Quality: {q['quality']} with {q['seeds']} seeds")
        mediumQuality = randomMovie["torrents"][0]
        highQuality = randomMovie["torrents"][1]
        if not highQuality:
            peerflix(randomMovie["torrents"][0]["url"], "mpchc", True)
        else:
            peerflix(randomMovie["torrents"][1]["url"], "mpchc", True)
        
        


