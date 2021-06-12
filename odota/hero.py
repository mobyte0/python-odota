import requests

URL = 'https://api.opendota.com/api/heroes/'


class Hero(object):
    def __init__(self, hero_id: int, api_key: str = ''):
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}
        self.URL = URL + str(hero_id) + '/'

    def matches(self):
        """Get recent matches with a hero"""
        data = requests.get(self.URL + 'matches', params=self.specs)
        return data.json()

    def matchups(self):
        """Get results against other heroes for a hero"""
        data = requests.get(self.URL + 'matchups', params=self.specs)
        return data.json()

    def durations(self):
        """Get hero performance over a range of match durations"""
        data = requests.get(self.URL + 'durations', params=self.specs)
        return data.json()

    def players(self):
        """Get players who have played this hero"""
        data = requests.get(self.URL + 'players', params=self.specs)
        return data.json()
