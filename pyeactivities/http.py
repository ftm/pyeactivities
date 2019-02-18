import os

import requests

ENDPOINT_BASE = os.environ["EACTIVITIES_API_ENDPOINT"]
DEFAULT_USER_AGENT = "pyeactivities/0.1.0"


class EActivitesClient:
    def __init__(self, api_key, user_agent=DEFAULT_USER_AGENT):
        self.api_key = api_key
        self.user_agent = user_agent

    def _get(self, endpoint):
        url = ENDPOINT_BASE + endpoint
        return requests.get(
            url,
            headers={"X-API-Key": self.api_key, "User-Agent": self.user_agent},
        )

    def get(self, endpoint):
        r = self._get(endpoint)

        return r.json()
