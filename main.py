import os
from search import Search

def clear():
    os.system('cls')

class Movie:
    def __init__(self, genre, rating):
        self.genre = genre
        self.rating = rating

    def searchMovie(self):
        print(f"Searching movie with the genre {self.genre} with the rating above {self.rating}...")
        movieSearch = Search(self.genre, self.rating)
        movieSearch.searchMovies()

def getInfo():
    hasCompleted = 0
    genre = input("Enter the genre for the movie (https://www.imdb.com/feature/genre/)\n")
    clear()
    rating = ""
    while hasCompleted == 0:
        rating = float(input("Enter the minimum rate for the movie (1-10)\n"))
        if rating < 0 or rating > 10:
            print("Please enter a valid rating value, it must be between 1 and 10")
        else:
            hasCompleted += 1
    clear()
    movie = Movie(genre, rating)
    movie.searchMovie()

def main():
    getInfo()

if __name__ == "__main__":
    print("This is a app made to get a random movie based on a genre")
    main()