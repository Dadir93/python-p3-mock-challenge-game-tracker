class Game:
    def __init__(self, title):
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = title

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all_results if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        game_results = [result.score for result in self.results() if result.player == player]
        if not game_results:
            return 0
        return sum(game_results) / len(game_results)


class Result:
    all_results = []

    def __init__(self, player, game, score):
        if not isinstance(score, int) or not (1 <= score <= 5000):
            raise ValueError("Score must be an integer between 1 and 5000.")
        self._player = player
        self._game = game
        self._score = score
        Result.all_results.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game
