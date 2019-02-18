from pyeactivities.http import EActivitesClient


class EActivities:
    def __init__(self, api_key: str):
        self.client = EActivitesClient(api_key)
