from pyeactivities.http import EActivitesClient


class CSP:
    """Represents a CSP as returned by the CSP endpoint"""

    def __init__(
        self,
        code: str,
        name: str,
        web_name: str,
        acronym: str,
        client: EActivitesClient,
    ):
        self.code = code
        self.name = name
        self.web_name = web_name
        self.acronym = acronym
        self.client = client

        self._members = None

    def get_members(self, force_recheck=False, save_results=True):
        if self._members and not force_recheck:
            return self._members

        # Query eActivities
        members_response = self.client.get("/CSP/{code}/reports/members".format(code=self.code))
        members = [
            Member(
                m["FirstName"],
                m["Surname"],
                m["CID"],
                m["Email"],
                m["Login"],
                m["OrderNo"],
                m["MemberType"],
            )
            for m in members_response
        ]

        if save_results:
            self._members = members

        return members

    def __repr__(self):
        return "CSP(code='{code}', name='{name}')".format(
            code=self.code, name=self.name
        )


class Member:
    def __init__(
        self,
        first_name: str,
        surname: str,
        cid: str,
        email: str,
        login: str,
        order_no: str,
        member_type: str,
    ):
        self.first_name = first_name
        self.surname = surname
        self.cid = cid
        self.email = email
        self.login = login
        self.order_no = order_no
        self.member_type = member_type


class CommitteeMember:
    """Represents a committee members as returned by the committee member endpoint"""

    def __init__(
        self,
        first_name: str,
        surname: str,
        cid: str,
        email: str,
        login: str,
        post_name: str,
        phone_no: str,
        start_date: str,
        end_date: str,
    ):
        self.first_name = first_name
        self.surname = surname
        self.cid = cid
        self.email = email
        self.login = login
        self.post_name = post_name
        self.phone_no = phone_no
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return "CommitteeMember(surname='{sn}', first_name='{fn}', cid={cid})".format(
            sn=self.surname, fn=self.first_name, cid=self.cid
        )
