"""
This file contains unit tests for each model

Test data has been taken from the eActivities API Documentation
"""


def test_csp_init(csp, client):
    assert csp.code == "170"
    assert csp.name == "RCC Ferret Fanciers (TEST CLUB)"
    assert csp.web_name == "Ferrets"
    assert csp.acronym == "RFF"
    assert csp.client == client


def test_member_init(member):
    assert member.first_name == "Joe"
    assert member.surname == "Bloggs"
    assert member.cid == "00000000"
    assert member.email == "joe.bloggs50@imperial.ac.uk"
    assert member.login == "jbloggs50"
    assert member.order_no == "1000"
    assert member.member_type == "Full"


def test_committee_member_init(committee_member):
    assert committee_member.first_name == "Joe"
    assert committee_member.surname == "Bloggs"
    assert committee_member.cid == "00000000"
    assert committee_member.email == "joe.bloggs50@imperial.ac.uk"
    assert committee_member.login == "jbloggs50"
    assert committee_member.post_name == "Chief Ferret Fancier"
    assert committee_member.phone_no == "02075948060"
    assert committee_member.start_date == "2014-08-01 00:00:00"
    assert committee_member.end_date == "2015-07-31 23:59:59"


def test_customer_init(customer):
    assert customer.first_name == "Joe"
    assert customer.surname == "Bloggs"
    assert customer.cid == "00000000"
    assert customer.email == "joe.bloggs50@imperial.ac.uk"
    assert customer.login == "jbloggs50"


def test_vat_init(vat):
    assert vat.code == "S1"
    assert vat.name == "S1 - Sales Standard Rated"
    assert vat.rate == 20


def test_online_sale_init(online_sale, customer, vat):
    assert online_sale.order_number == "1000"
    assert online_sale.sale_date_time == "2015-06-20 19:00:00"
    assert online_sale.product_id == 1234
    assert online_sale.product_line_id == 4567
    assert online_sale.price == 30
    assert online_sale.quantity == 1
    assert online_sale.quantity_collected == 0
    assert online_sale.customer == customer
    assert online_sale.vat == vat


def test_account_init(account):
    assert account.code == "580"
    assert account.name == "Ticket Income (580)"
    assert account.type == "Income"


def test_activity_init(activity):
    assert activity.code == "00"
    assert activity.name == "General (0)"


def test_product_line_init(product_line, account, activity, vat):
    assert product_line.id == 4567
    assert product_line.name == "Ferret Annual Dinner Ticket"
    assert product_line.quantity is None
    assert product_line.unlimited is True
    assert product_line.price == 30
    assert product_line.collectable is False
    assert product_line.default_option is True
    assert product_line.account == account
    assert product_line.activity == activity
    assert product_line.vat == vat


def test_product_init(product, csp, product_line):
    assert product.csp == csp
    assert product.id == 1234
    assert product.name == "Ferret Fanciers Annual Dinner 2015"
    assert product.description == "Tickets for our Annual Dinner 2015"
    assert product.type == "World - Products available to everyone including non-Imperial students and staff"
    assert product.selling_date_start == "2015-06-01 00:00:00"
    assert product.selling_date_end == "2015-06-30 00:00:00"
    assert product.url == "https://www.imperialcollegeunion.org/shop/club-society-project-products/ferrets-products/1234/ferret-annual-dinner-2015"
    assert product.active is True
    assert product.product_lines == [product_line]
