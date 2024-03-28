from classes.many_to_many import Result
from classes.many_to_many import Game

class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = username
        self._player_results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("Username must be a string.")
        if 2 <= len(new_username) <= 16:
            self._username = new_username

    def results(self):
        return self._player_results

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)
