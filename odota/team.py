import requests

URL = 'https://api.opendota.com/api/teams/'


class Team(object):
    def __init__(self, team_id: int, api_key: str = ''):
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}
        self.URL = URL + str(team_id)

    def team(self):
        """Get data for a team"""
        data = requests.get(self.URL, params=self.specs)
        return data.json()

    def matches(self):
        """Get matches for a team"""
        data = requests.get(self.URL + '/matches', params=self.specs)
        return data.json()

    def players(self):
        """Get players who have played for a team"""
        data = requests.get(self.URL + '/players', params=self.specs)
        return data.json()

    def heroes(self):
        """Get heroes for a team"""
        data = requests.get(self.URL + '/heroes', params=self.specs)
        return data.json()
