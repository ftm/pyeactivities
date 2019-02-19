import os

from pyeactivities.eactivities import EActivities

eactivities = EActivities(os.environ["EACTIVITIES_API_KEY"], os.environ["EACTIVITIES_API_ENDPOINT"])

my_csp = eactivities.get_csps()[0]

print(
    "Generating a member report for: {name} ({code})".format(
        name=my_csp.name, code=my_csp.code
    )
)

members = my_csp.get_members()

member_count = len(members)
full_member_count = 0
for m in members:
    if m.member_type == "Full":
        full_member_count += 1
other_members_count = member_count - full_member_count

print(
    "CSP Members: {count} (full: {s_count}, other: {o_count})".format(
        count=member_count, s_count=full_member_count, o_count=other_members_count
    )
)

for m in members:
    print(
        "  {cid} - {fn} {sn} ({type})".format(
            cid=m.cid, fn=m.first_name, sn=m.surname, type=m.member_type
        )
    )
