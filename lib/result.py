class Player:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise ValueError("Username must be a string.")
        if not 2 <= len(new_username) <= 16:
            raise ValueError("Username must be between 2 and 16 characters long.")
        self._username = new_username

    def results(self):
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)
