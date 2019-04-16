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

products = my_csp.get_products()

print("Products: {}".format(len(products)))

for p in products:
    print("  {productid} - {name}".format(productid=p.id, name=p.name))
    p_sales = p.get_sales()
    for s in p_sales:
        print("    {s}".format(s=s))
