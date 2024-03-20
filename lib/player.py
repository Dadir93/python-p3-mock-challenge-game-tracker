from game import Result

class Player:
    def __init__(self, username):
        if not isinstance(username, str) or not (2 <= len(username) <= 16):
            raise ValueError("Username must be a string between 2 and 16 characters.")
        self._username = username

    @property
    def username(self):
        return self._username

    def results(self):
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)
