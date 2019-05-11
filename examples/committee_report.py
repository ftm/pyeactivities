import os

from pyeactivities import EActivities

eactivities = EActivities(
    os.environ["EACTIVITIES_API_KEY"], os.environ["EACTIVITIES_API_ENDPOINT"]
)

my_csp = eactivities.get_csps()[0]

print(
    "Generating a committee report for: {name} ({code})".format(
        name=my_csp.name, code=my_csp.code
    )
)

committee = my_csp.get_committee_members()

print("Committee Members: {}".format(len(committee)))


for c in committee:
    print(
        "  {cid} - {fn} {sn} ({post})".format(
            cid=c.cid, fn=c.first_name, sn=c.surname, post=c.post_name
        )
    )
