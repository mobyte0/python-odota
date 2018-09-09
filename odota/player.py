import requests

URL = 'https://api.opendota.com/api/players/'


class Player(object):
    """
    parameter reference:
    limit -- number of matches to limit to
    offset -- number of matches to offset start by
    win -- 0 for lost match, 1 for won match
    patch -- index of patch number from here:
        https://github.com/odota/dotaconstants/blob/master/build/patch.json
    game_mode --
        https://github.com/odota/dotaconstants/blob/master/build/game_mode.json
    lobby_type --
        https://github.com/odota/dotaconstants/blob/master/build/lobby_type.json
    region --
        https://github.com/odota/dotaconstants/blob/master/build/region.json
    date -- days previous, i.e. 7 is last week, 30 is last month, etc.
    lane_role -- 0 for unknown, 1 for safe, 2 for mid, 3 for off, 4 for jungle
    hero_id --
        https://github.com/odota/dotaconstants/blob/master/build/heroes.json
    is_radiant -- 0 for dire, 1 for radiant
    included_account_id -- account ids in the match
    excluded_account_id -- account ids not in the match
    with_hero_id -- hero id on the player team, see hero_id above
    against_hero_id -- hero id on the enemy team, see hero_id above
    significant -- whether the match was significant for aggregation purposes,
        0 to include insignificant matches
    having -- minimum number of games played
    sort -- field to return matches sorted by in descending order
    project -- fields to project
    field -- valid options: kills, actions_per_min, assists, comeback,
        courier_kills, deaths, denies, duration, lane_efficiency_pct,
        purchase_gem, gold_per_min, hero_damage, hero_healing, kda, last_hits,
        level, loss, pings, neutral_kills, purchase_ward_observer,
        purchase_rapier, purchase_ward_sentry, stomp, stuns, throw,
        tower_damage, tower_kills, purchase_tpscroll, xp_per_min
    """

    def __init__(self, account_id: int, api_key: str = ''):
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}
        self.URL = URL + str(account_id)

    def player(self):
        """Get player data"""
        data = requests.get(self.URL + self.api_key)
        return data.json()

    def wl(self, limit: int = None, offset: int = None, win: int = None,
           patch: int = None, game_mode: int = None, lobby_type: int = None,
           region: int = None, date: int = None, lane_role: int = None,
           hero_id: int = None, is_radiant: int = None,
           included_account_id: list = None, excluded_account_id: list = None,
           with_hero_id: list = None, against_hero_id: list = None,
           significant: int = None, having: int = None, sort: str = None):
        """Win/Loss count"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/wl', self.specs)
        return data.json()

    def recentMatches(self):
        """Recent matches played"""
        data = requests.get(self.URL + '/recentMatches', self.specs)
        return data.json()

    def matches(self, limit: int = None, offset: int = None, win: int = None,
                patch: int = None, game_mode: int = None,
                lobby_type: int = None,
                region: int = None, date: int = None, lane_role: int = None,
                hero_id: int = None, is_radiant: int = None,
                included_account_id: list = None,
                excluded_account_id: list = None,
                with_hero_id: list = None, against_hero_id: list = None,
                significant: int = None, having: int = None, sort: str = None,
                project: str = None):
        """Get matches played by player"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort, 'project': project}
        data = requests.get(self.URL + '/matches', self.specs)
        return data.json()

    def heroes(self, limit: int = None, offset: int = None, win: int = None,
               patch: int = None, game_mode: int = None,
               lobby_type: int = None,
               region: int = None, date: int = None, lane_role: int = None,
               hero_id: int = None, is_radiant: int = None,
               included_account_id: list = None,
               excluded_account_id: list = None,
               with_hero_id: list = None, against_hero_id: list = None,
               significant: int = None, having: int = None, sort: str = None):
        """Get heroes played by player"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/heroes', self.specs)
        return data.json()

    def peers(self, limit: int = None, offset: int = None, win: int = None,
              patch: int = None, game_mode: int = None,
              lobby_type: int = None,
              region: int = None, date: int = None, lane_role: int = None,
              hero_id: int = None, is_radiant: int = None,
              included_account_id: list = None,
              excluded_account_id: list = None,
              with_hero_id: list = None, against_hero_id: list = None,
              significant: int = None, having: int = None, sort: str = None):
        """Get players played with"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/peers', self.specs)
        return data.json()

    def pros(self, limit: int = None, offset: int = None, win: int = None,
             patch: int = None, game_mode: int = None,
             lobby_type: int = None,
             region: int = None, date: int = None, lane_role: int = None,
             hero_id: int = None, is_radiant: int = None,
             included_account_id: list = None,
             excluded_account_id: list = None,
             with_hero_id: list = None, against_hero_id: list = None,
             significant: int = None, having: int = None, sort: str = None):
        """Get pro players played with"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/pros', self.specs)
        return data.json()

    def totals(self, limit: int = None, offset: int = None, win: int = None,
               patch: int = None, game_mode: int = None,
               lobby_type: int = None,
               region: int = None, date: int = None, lane_role: int = None,
               hero_id: int = None, is_radiant: int = None,
               included_account_id: list = None,
               excluded_account_id: list = None,
               with_hero_id: list = None, against_hero_id: list = None,
               significant: int = None, having: int = None, sort: str = None):
        """Totals in stats"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/totals', self.specs)
        return data.json()

    def counts(self, limit: int = None, offset: int = None, win: int = None,
               patch: int = None, game_mode: int = None,
               lobby_type: int = None,
               region: int = None, date: int = None, lane_role: int = None,
               hero_id: int = None, is_radiant: int = None,
               included_account_id: list = None,
               excluded_account_id: list = None,
               with_hero_id: list = None, against_hero_id: list = None,
               significant: int = None, having: int = None, sort: str = None):
        """Counts in categories"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/counts', self.specs)
        return data.json()

    def histograms(self, field: str, limit: int = None, offset: int = None,
                   win: int = None,
                   patch: int = None, game_mode: int = None,
                   lobby_type: int = None,
                   region: int = None, date: int = None, lane_role: int = None,
                   hero_id: int = None, is_radiant: int = None,
                   included_account_id: list = None,
                   excluded_account_id: list = None,
                   with_hero_id: list = None, against_hero_id: list = None,
                   significant: int = None, having: int = None,
                   sort: str = None):
        """Distribution of matches in a single stat"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/histograms/' + field, self.specs)
        return data.json()

    def wardmap(self, limit: int = None, offset: int = None, win: int = None,
                patch: int = None, game_mode: int = None,
                lobby_type: int = None,
                region: int = None, date: int = None, lane_role: int = None,
                hero_id: int = None, is_radiant: int = None,
                included_account_id: list = None,
                excluded_account_id: list = None,
                with_hero_id: list = None, against_hero_id: list = None,
                significant: int = None, having: int = None,
                sort: str = None):
        """Wards placed in matches played"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/wardmap', self.specs)
        return data.json()

    def wordcloud(self, limit: int = None, offset: int = None,
                  win: int = None,
                  patch: int = None, game_mode: int = None,
                  lobby_type: int = None,
                  region: int = None, date: int = None, lane_role: int = None,
                  hero_id: int = None, is_radiant: int = None,
                  included_account_id: list = None,
                  excluded_account_id: list = None,
                  with_hero_id: list = None, against_hero_id: list = None,
                  significant: int = None, having: int = None,
                  sort: str = None):
        """Words said/read in matches played"""
        self.specs = {'api_key': self.api_key, 'limit': limit,
                      'offset': offset, 'win': win, 'patch': patch,
                      'game_mode': game_mode, 'lobby_type': lobby_type,
                      'region': region, 'date': date, 'lane_role': lane_role,
                      'hero_id': hero_id, 'is_radiant': is_radiant,
                      'included_account_id': included_account_id,
                      'excluded_account_id': excluded_account_id,
                      'with_hero_id': with_hero_id,
                      'against_hero_id': against_hero_id,
                      'significant': significant, 'having': having,
                      'sort': sort}
        data = requests.get(self.URL + '/wordcloud', self.specs)
        return data.json()

    def ratings(self):
        """Player rating history"""
        data = requests.get(self.URL + '/ratings', self.specs)
        return data.json()

    def rankings(self):
        """Player hero rankings"""
        data = requests.get(self.URL + '/rankings', self.specs)
        return data.json()

    def refresh(self):
        """Refresh player match history"""
        data = requests.post(self.URL + '/refresh', self.specs)
        return data.json()
