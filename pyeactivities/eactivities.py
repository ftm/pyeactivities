from typing import List

from pyeactivities.http import EActivitiesClient
from pyeactivities.models import CSP


class EActivities:
    """
    This is the entry point into the eActivities API. It is used to retrieve the
    CSP objects you use to access most of the rest of the API.
    """

    def __init__(self, api_key: str, endpoint_base: str):
        self.client = EActivitiesClient(api_key, endpoint_base)

    def get_csps(self) -> List[CSP]:
        """
        Retrieve the list of CSP objects that the API key has access to
        """
        csps_response = self.client.get("/CSP")
        return [
            CSP(csp["Code"], csp["Name"], csp["WebName"], csp["Acronym"], self.client)
            for csp in csps_response
        ]
