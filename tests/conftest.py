import pytest

from pyeactivities import (
    CSP,
    Member,
    CommitteeMember,
    OnlineSale,
    Customer,
    VAT,
    Product,
    ProductLine,
    Account,
    Activity,
)

from tests.util.dummy_client import DummyClient

"""
This file contains the fixtures used for testing

Test data has been taken from the eActivities API Documentation
"""


@pytest.fixture()
def client():
    return DummyClient()


@pytest.fixture()
def csp(client):
    return CSP("170", "RCC Ferret Fanciers (TEST CLUB)", "Ferrets", "RFF", client)


@pytest.fixture()
def member():
    return Member(
        "Joe",
        "Bloggs",
        "00000000",
        "joe.bloggs50@imperial.ac.uk",
        "jbloggs50",
        "1000",
        "Full",
    )


@pytest.fixture()
def committee_member():
    return CommitteeMember(
        "Joe",
        "Bloggs",
        "00000000",
        "joe.bloggs50@imperial.ac.uk",
        "jbloggs50",
        "Chief Ferret Fancier",
        "02075948060",
        "2014-08-01 00:00:00",
        "2015-07-31 23:59:59",
    )


@pytest.fixture()
def customer():
    return Customer(
        "Joe", "Bloggs", "00000000", "joe.bloggs50@imperial.ac.uk", "jbloggs50"
    )


@pytest.fixture()
def vat():
    return VAT("S1", "S1 - Sales Standard Rated", 20)


@pytest.fixture()
def online_sale(customer, vat):
    return OnlineSale(
        "1000", "2015-06-20 19:00:00", 1234, 4567, 30, 1, 0, customer, vat
    )


@pytest.fixture()
def account():
    return Account("580", "Ticket Income (580)", "Income")


@pytest.fixture()
def activity():
    return Activity("00", "General (0)")


@pytest.fixture()
def product_line(account, activity, vat):
    return ProductLine(
        4567,
        "Ferret Annual Dinner Ticket",
        None,
        True,
        30,
        False,
        True,
        account,
        activity,
        vat,
    )


@pytest.fixture()
def product(product_line, csp):
    return Product(
        csp,
        1234,
        "Ferret Fanciers Annual Dinner 2015",
        "Tickets for our Annual Dinner 2015",
        "World - Products available to everyone including non-Imperial students and staff",
        "2015-06-01 00:00:00",
        "2015-06-30 00:00:00",
        "https://www.imperialcollegeunion.org/shop/club-society-project-products/ferrets-products/1234/ferret-annual-dinner-2015",
        True,
        [product_line],
    )