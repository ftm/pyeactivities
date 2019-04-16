import requests

DEFAULT_USER_AGENT = "pyeactivities/0.1.0"


class EActivitesClient:
    def __init__(self, api_key, endpoint_base, user_agent=DEFAULT_USER_AGENT):
        self.api_key = api_key
        self.endpoint_base = endpoint_base
        self.user_agent = user_agent

    def _get(self, endpoint):
        url = self.endpoint_base + endpoint
        return requests.get(
            url, headers={"X-API-Key": self.api_key, "User-Agent": self.user_agent}
        )

    def get(self, endpoint):
        r = self._get(endpoint)

        return r.json()
