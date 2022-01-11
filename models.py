import json


class Movies:
    def __init__(self):
        try:
            with open("movies.json", "r") as f:
                self.movies = json.load(f)
        except FileNotFoundError:
            self.movies = []

    def all(self):
        return self.movies

    def get(self, id):
        return self.movies[id]

    def create(self, data):
        data.pop('csrf_token')
        self.movies.append(data)

    def save_all(self):
        with open("movies.json", "w") as f:
            json.dump(self.movies, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.movies[id] = data
        self.save_all()


movies = Movies()