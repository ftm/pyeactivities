from typing import List

from pyeactivities.http import EActivitesClient
from pyeactivities.models import CSP


class EActivities:
    def __init__(self, api_key: str, endpoint_base: str):
        self.client = EActivitesClient(api_key, endpoint_base)

    def get_csps(self) -> List[CSP]:
        csps_response = self.client.get("/CSP")
        return [CSP(csp["Code"], csp["Name"], csp["WebName"], csp["Acronym"], self.client) for csp in csps_response]
