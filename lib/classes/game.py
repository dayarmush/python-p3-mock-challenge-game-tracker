class Game:
    def __init__(self, title):
        self.title = title
        self.results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if len(new_title) > 0:
            self._title = new_title
        else:
            raise Exception('invalid title')
        
    def get_players(self):
        return [results.player for results in self.results]
    
    def average_score(self, player):
        count = 0
        for result in self.results:
            if result.player == player:
                count += result.score
            else:
                continue

        return count / len(self.results)
        