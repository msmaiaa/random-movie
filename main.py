import os
from search import Search

def clear():
    os.system('cls')

def getParams():
    hasCompleted = 0
    genre = input("Enter the genre for the movie (https://www.imdb.com/feature/genre/)\n")
    clear()
    rating = ""
    while hasCompleted == 0:
        rating = float(input("Enter the minimum rating for the movie (0-10)\n"))
        if rating < 0 or rating > 10:
            print("Please enter a valid rating value, it must be between 0 and 10")
        else:
            hasCompleted += 1
    clear()
    movie = Movie(genre, rating)
    movie.handleMovie()

class Movie:
    def __init__(self, genre, rating):
        self.genre = genre
        self.rating = rating

    def handleMovie(self):
        print(f"Searching movie with the genre {self.genre} with the rating above {self.rating}...")
        movieSearch = Search(self.genre, self.rating)
        movieSearch.handleMovieParams()

def main():
    getParams()

if __name__ == "__main__":
    main()