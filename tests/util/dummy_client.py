from pyeactivities.http import EActivitesClient


class DummyClient(EActivitesClient):
    def __init__(self):
        super(DummyClient, self).__init__("DUMMY", "dummy")

    def _get(self, endpoint):
        print("Attempting to get endpoint:", endpoint)
