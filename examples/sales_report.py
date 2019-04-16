import os

from pyeactivities.eactivities import EActivities

eactivities = EActivities(
    os.environ["EACTIVITIES_API_KEY"], os.environ["EACTIVITIES_API_ENDPOINT"]
)

my_csp = eactivities.get_csps()[0]

print(
    "Generating a sales report for: {name} ({code})".format(
        name=my_csp.name, code=my_csp.code
    )
)

sales = my_csp.get_online_sales()

print("Sales Records: {}".format(len(sales)))


for s in sales:
    print(
        "  {orderno} - {product} - {fn} {sn}".format(
            orderno=s.order_number,
            product=s.product_id,
            fn=s.customer.first_name,
            sn=s.customer.surname,
        )
    )
