from classes.many_to_many import Result

class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = title
        self._game_results = []

    @property
    def title(self):
        return self._title

    def results(self):
        return self._game_results

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        player_results = [result.score for result in self.results() if result.player == player]
        if not player_results:
            return None
        return sum(player_results) / len(player_results)
