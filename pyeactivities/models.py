from typing import List

from pyeactivities.http import EActivitesClient


class CSP:
    """
    Represents a CSP as returned by the CSP endpoint
    """

    def __init__(
        self,
        code: str,
        name: str,
        web_name: str,
        acronym: str,
        client: EActivitesClient,
    ):
        self.code = code
        """The (typically 3 digit) code for the CSP"""
        self.name = name
        """The name of the CSP"""
        self.web_name = web_name
        """The name of the society as listed on the Union's website"""
        self.acronym = acronym
        """The acronym of the society"""
        self.client = client
        """The EActivitiesClient to use for API requests"""

        # Cache objects
        self._members = None
        self._committee_members = None
        self._online_sales = None
        self._products = None

    def get_members(self, force_recheck=False, save_results=True):
        """
        Retrieve a list of of the CSP's members

        :param force_recheck: override the CSP's cache
        :param save_results: save the respones to the CSP's cache
        """
        # Check if we have a cached list and we aren't overriding
        if self._members and not force_recheck:
            return self._members

        # Retrieve list of members from eActivities and parse
        members_response = self._csp_get("reports/members")
        members = [Member.from_dict(m) for m in members_response]

        # Save results into cache if requested
        if save_results:
            self._members = members

        return members

    def get_committee_members(self, force_recheck=False, save_results=True):
        """
        Retrieve a list of the CSP's committee members

        :param force_recheck: override the CSP's cache
        :param save_results: save the respones to the CSP's cache
        """
        if self._committee_members and not force_recheck:
            return self._committee_members

        committee_response = self._csp_get("reports/committee")
        committee = [CommitteeMember.from_dict(c) for c in committee_response]

        if save_results:
            self._committee_members = committee

        return committee

    def get_online_sales(self, force_recheck=False, save_results=True):
        """
        Retrieve all of the CSP's online sales

        :param force_recheck: override the CSP's cache
        :param save_results: save the respones to the CSP's cache
        """
        if self._online_sales and not force_recheck:
            return self._online_sales

        sales_response = self._csp_get("reports/onlinesales")
        sales = [OnlineSale.from_dict(s) for s in sales_response]

        if save_results:
            self._online_sales = sales

        return sales

    def get_products(self, force_recheck=False, save_results=True):
        """
        Retrieve all of the CSP's shop products

        :param force_recheck: override the CSP's cache
        :param save_results: save the respones to the CSP's cache
        """
        if self._products and not force_recheck:
            return self._products

        product_response = self._csp_get("reports/products")
        products = [Product.from_dict(self, p) for p in product_response]

        if save_results:
            self._products = products

        return products

    def get_product(self, id):
        # /csp/{centre}/products/{id}
        pass

    def _make_url(self, path):
        return "/CSP/{code}/{path}".format(code=self.code, path=path)

    def _csp_get(self, path):
        return self.client.get(self._make_url(path))

    def __repr__(self):
        return "CSP(code='{code}', name='{name}')".format(
            code=self.code, name=self.name
        )


class Member:
    """
    Represents a member of a CSP as returned by the member report endpoint
    """

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

    @staticmethod
    def from_dict(m):
        return Member(
            m["FirstName"],
            m["Surname"],
            m["CID"],
            m["Email"],
            m["Login"],
            m["OrderNo"],
            m["MemberType"],
        )

    def __repr__(self):
        return "Member(surname='{sn}', first_name='{fn}', cid={cid})".format(
            sn=self.surname, fn=self.first_name, cid=self.cid
        )


class CommitteeMember:
    """
    Represents a committee member of a CSP as returned by the committee member
    report endpoint
    """

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

    @staticmethod
    def from_dict(c):
        return CommitteeMember(
            c["FirstName"],
            c["Surname"],
            c["CID"],
            c["Email"],
            c["Login"],
            c["PostName"],
            c["PhoneNo"],
            c["StartDate"],
            c["EndDate"],
        )

    def __repr__(self):
        return "CommitteeMember(surname='{sn}', first_name='{fn}', cid={cid})".format(
            sn=self.surname, fn=self.first_name, cid=self.cid
        )


class Customer:
    """
    Represents a customer from an online sale
    """

    def __init__(self, first_name: str, surname: str, cid: str, email: str, login: str):
        self.first_name = first_name
        self.surname = surname
        self.cid = cid
        self.email = email
        self.login = login

    @staticmethod
    def from_dict(c):
        return Customer(c["FirstName"], c["Surname"], c["CID"], c["Email"], c["Login"])


class VAT:
    """
    Represents the VAT information for a product or sale etc.
    """

    def __init__(self, code: str, name: str, rate: float):
        self.code = code
        self.name = name
        self.rate = rate

    @staticmethod
    def from_dict(v):
        return VAT(v["Code"], v["Name"], v["Rate"])


class OnlineSale:
    """
    Represents an online sale with details of the product, price, and customer
    """

    def __init__(
        self,
        order_number: str,
        sale_date_time: str,
        product_id: int,
        product_line_id: int,
        price: float,
        quantity: int,
        quantity_collected: int,
        customer: Customer,
        vat: VAT,
    ):
        self.order_number = order_number
        self.sale_date_time = sale_date_time
        self.product_id = product_id
        self.product_line_id = product_line_id
        self.price = price
        self.quantity = quantity
        self.quantity_collected = quantity_collected
        self.customer = customer
        self.vat = vat

    @staticmethod
    def from_dict(s):
        return OnlineSale(
            s["OrderNumber"],
            s["SaleDateTime"],
            s["ProductID"],
            s["ProductLineID"],
            s["Price"],
            s["Quantity"],
            s["QuantityCollected"],
            Customer.from_dict(s["Customer"]),
            VAT.from_dict(s["VAT"]),
        )


class Account:
    """
    Represents an account within a CSP's finances
    """

    def __init__(self, code: str, name: str, type: str):
        self.code = code
        self.name = name
        self.type = type

    @staticmethod
    def from_dict(a):
        return Account(a["Code"], a["Name"], a["Type"])


class Activity:
    """
    Represents an activity within a CSP's finances
    """

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name

    @staticmethod
    def from_dict(a):
        return Activity(a["Code"], a["Name"])


class ProductLine:
    """
    Represents a particular line within a product sold on the CSP's online shop
    """

    def __init__(
        self,
        id: int,
        name: str,
        quantity: int,
        unlimited: bool,
        price: float,
        collectable: bool,
        default_option: bool,
        account: Account,
        activity: Activity,
        vat: VAT,
    ):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unlimited = unlimited
        self.price = price
        self.collectable = collectable
        self.default_option = default_option
        self.account = account
        self.activity = activity
        self.vat = vat

    @staticmethod
    def from_dict(l):
        return ProductLine(
            l["ID"],
            l["Name"],
            l["Quantity"],
            l["Unlimited"],
            l["Price"],
            l["Collectable"],
            l["DefaultOption"],
            Account.from_dict(l["Account"]),
            Activity.from_dict(l["Activity"]),
            VAT.from_dict(l["VAT"]),
        )


class Product:
    """
    Represents a product sold on the online shop
    """

    def __init__(
        self,
        csp: CSP,
        id: int,
        name: str,
        description: str,
        type: str,
        selling_date_start: str,
        selling_date_end: str,
        url: str,
        active: bool,
        product_lines: List[ProductLine],
    ):
        self.csp = csp
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.selling_date_start = selling_date_start
        self.selling_date_end = selling_date_end
        self.url = url
        self.active = active
        self.product_lines = product_lines

        self._sales = None

    def get_sales(self, force_recheck=False, save_results=True) -> List[OnlineSale]:
        """
        Retrieve a list of sales for the product

        :param force_recheck: override the CSP's cache
        :param save_results: save the respones to the CSP's cache
        """
        if self._sales and not force_recheck:
            return self._sales

        sales_response = self.csp._csp_get("products/{id}/sales".format(id=self.id))

        if type(sales_response) is not list:
            return []

        sales = [OnlineSale.from_dict(s) for s in sales_response]

        if save_results:
            self._sales = sales

        return sales

    @staticmethod
    def from_dict(csp, p):
        return Product(
            csp,
            p["ID"],
            p["Name"],
            p["Description"],
            p["Type"],
            p["SellingDateStart"],
            p["SellingDateEnd"],
            p["URL"],
            p["Active"],
            [ProductLine.from_dict(l) for l in p["ProductLines"]],
        )
