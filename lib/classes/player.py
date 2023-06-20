class Player:
    def __init__(self, username):
        self.username = username
        self.results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception('invalid username')
    
    def games_played(self):
        return [result.game for result in self.results]
    
    def has_played_game(self, game):
        has_game = [result for result in self.results if result.game == game]
        return not not has_game
    
    def num_times_played(self, game):
        counter = 0 
        for result in self.results:
            if result.game == game:
                counter += 1
        return counter

