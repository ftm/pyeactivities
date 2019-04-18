import requests

from pyeactivities import __version__ as pyeactivities_version
from pyeactivities.exceptions import (
    APIException,
    APIUnauthorisedException,
    APIForbiddenException,
)

DEFAULT_USER_AGENT = "pyeactivities/{}".format(pyeactivities_version)


class EActivitesClient:
    def __init__(self, api_key, endpoint_base, user_agent=DEFAULT_USER_AGENT):
        self.api_key = api_key
        self.endpoint_base = endpoint_base
        self.user_agent = user_agent

    def _get(self, endpoint):
        url = self.endpoint_base + endpoint
        r = requests.get(
            url, headers={"X-API-Key": self.api_key, "User-Agent": self.user_agent}
        )

        if r.status_code == 200:
            return r
        elif r.status_code == 401:
            raise APIUnauthorisedException(
                "API returned status code 401 - are you using a correct API key?"
            )
        elif r.status_code == 403:
            raise APIForbiddenException(
                "API returned status code 403 - too many requests and/or too many repeated failed attempts"
            )
        else:
            raise APIException("API returned status code {}".format(r.status_code))

    def get(self, endpoint):
        r = self._get(endpoint)

        return r.json()
