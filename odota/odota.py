import requests

URL = 'https://api.opendota.com/api/'


class Load(object):
    """
    parameter reference:
    field -- valid options: kills, actions_per_min, assists, comeback,
        courier_kills, deaths, denies, duration, lane_efficiency_pct,
        purchase_gem, gold_per_min, hero_damage, hero_healing, kda, last_hits,
        level, loss, pings, neutral_kills, purchase_ward_observer,
        purchase_rapier, purchase_ward_sentry, stomp, stuns, throw,
        tower_damage, tower_kills, purchase_tpscroll, xp_per_min
    lane_role -- 1 is safe, 2 is mid, 3 is off, 4 is jungle
    scenario -- valid options: pos_char_1min, neg_chat_1min, courier_kill,
        first_blood
    """

    def __init__(self, api_key: str = ''):
        if api_key is '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}

    def match(self, match_id: int):
        """Get match data"""
        data = requests.get(URL + 'matches/' + str(match_id),
                            params=self.specs)
        return data.json()

    def proMatches(self, less_than_match_id: int = None):
        """Get list of pro matches"""
        self.specs['less_than_match_id'] = less_than_match_id
        data = requests.get(URL + 'proMatches', params=self.specs)
        return data.json()

    def publicMatches(self, mmr_ascending: int = None,
                      mmr_descending: int = None,
                      less_than_match_id: int = None):
        """Get list of randomly sampled public matches"""
        self.specs = {'api_key': self.api_key, 'mmr_ascending': mmr_ascending,
                      'mmr_descending': mmr_descending,
                      'less_than_match_id': less_than_match_id}
        data = requests.get(URL + 'publicMatches', params=self.specs)
        return data.json()

    def explorer(self, sql: str = None):
        """Submit arbitrary SQL queries to the database"""
        self.specs['sql'] = sql
        data = requests.get(URL + 'explorer', params=self.specs)
        return data.json()

    def search(self, query: str):
        """Search players by personaname"""
        self.specs['q'] = query
        data = requests.get(URL + 'search', params=self.specs)
        return data.json()

    def rankings(self, hero_id: str):
        """Top players by hero"""
        self.specs['hero_id'] = hero_id
        data = requests.get(URL + 'rankings', params=self.specs)
        return data.json()

    def benchmarks(self, hero_id: str):
        """Benchmarks of average stat values for a hero"""
        self.specs['hero_id'] = hero_id
        data = requests.get(URL + 'benchmarks', params=self.specs)
        return data.json()

    def request_job(self, job_id: str):
        """Get parse request state"""
        data = requests.get(URL + 'request/' + job_id, params=self.specs)
        return data.json()

    def request_match(self, match_id: int):
        """Submit a new parse request"""
        data = requests.post(URL + 'request/' + str(match_id),
                             params=self.specs)
        return data.json()

    def replays(self, match_id: int):
        """Get data to construct a replay URL with"""
        self.specs['match_id'] = str(match_id)
        data = requests.get(URL + 'replays', params=self.specs)
        return data.json()

    def records(self, field: str):
        """Get top performances in a stat"""
        data = requests.get(URL + 'records/' + field, params=self.specs)
        return data.json()

    def itemTimings(self, item: str = None, hero_id: int = None):
        """Win rates for certain item timings on a hero for items that cost at
        least 1400 gold"""
        self.specs = {'api_key': self.api_key, 'item': item,
                      'hero_id': hero_id}
        data = requests.get(URL + 'scenarios/itemTimings', params=self.specs)
        return data.json()

    def laneRoles(self, lane_role: str = None, hero_id: int = None):
        """Win rates for heroes in certain lane roles"""
        self.specs = {'api_key': self.api_key, 'lane_role': lane_role,
                      'hero_id': hero_id}
        data = requests.get(URL + 'scenarios/laneRoles', params=self.specs)
        return data.json()

    def miscScenarios(self, scenario: str = None):
        """Miscellaneous team scenarios"""
        self.specs = {'api_key': self.api_key, 'scenario': scenario}
        data = requests.get(URL + 'scenarios/misc', params=self.specs)
        return data.json()

    def live(self):
        """Get top currently ongoing live games"""
        data = requests.get(URL + 'live', params=self.specs)
        return data.json()

    def heroStats(self):
        """Get stats about hero performance in recent matches"""
        data = requests.get(URL + 'heroStats', params=self.specs)
        return data.json()

    def leagues(self):
        """Get league data"""
        data = requests.get(URL + 'leagues', params=self.specs)
        return data.json()

    def heroes(self):
        """Get hero data"""
        data = requests.get(URL + 'heroes', params=self.specs)
        return data.json()

    def metadata(self):
        """Site metadata"""
        data = requests.get(URL + 'metadata', params=self.specs)
        return data.json()

    def teams(self):
        """Get team data"""
        data = requests.get(URL + 'teams', params=self.specs)
        return data.json()

    def distributions(self):
        """Distributions of MMR data by bracket and country"""
        data = requests.get(URL + 'distributions', params=self.specs)
        return data.json()

    def proPlayers(self):
        """Get list of pro players"""
        data = requests.get(URL + 'proPlayers', params=self.specs)
        return data.json()

    def status(self):
        """Get current service statistics"""
        data = requests.get(URL + 'status', params=self.specs)
        return data.json()

    def apiMetrics(self):
        """Get API request metrics"""
        data = requests.get(URL + 'admin/apiMetrics', params=self.specs)
        return data.json()

    def health(self):
        """Get service health data"""
        data = requests.get(URL + 'health', params=self.specs)
        return data.json()

    def schema(self):
        """Get database schema"""
        data = requests.get(URL + 'schema', params=self.specs)
        return data.json()
