=============
pyeactivities
=============
.. currentmodule:: pyeactivities

pyeactivities provides a simple Python wrapper around the API for eActivites,
the system used by Imperial College Union for societies to manage themselves.
It handles tasks such as retrieving lists of members, lists of products, and
sales data from the society's shop.

Installation
============
Install the extension with pip::

    $ pip install pyeactivities-ftm

Usage
=====
In order to use pyeactivities, you will need an eActivities API key, and the
eActivities endpoint URL.

.. note::
  To obtain an API key, log in to eActivities and go to the details page for your
  society (where you can find a list of members), and click on "API Keys". On this
  page you can see the API keys that already exist for your society, as well as
  generate new ones. We recommend using a new API key for each application so they
  aren't shared.

  The eActivities endpoint URL can be found in the eActivities API documentation
  which you can download from the API Key page.

Create a new eActivities object like so, specifying the API key and endpoint
URL.

.. code-block:: python

  from pyeactivities.eactivities import EActivities

  # Base URL must end in trailing / (e.g. https://<eactivities>/API/)
  eactivities = EActivities(api_key, api_base_url)

You can then get a reference to your society by using:

.. code-block:: python

  csp = eactivities.get_csps()[0]

.. warning::
  :py:meth:`~pyeactivities.eactivities.EActivities.get_csps` can return multiple CSPs. The eActivities API implies that
  one API key could be used with multiple societies but that doesn't seem to be
  to be implemented yet so it's safe to just get the first one. Therefore, we
  recommend double checking you have access to the CSP you were expecting.

  .. code-block:: python

    if csp.code != "999":
      raise Exception("Unexpected CSP for given API key")

Most operations are then performed on this CSP object, for example:

.. code-block:: python

  members = csp.get_members()

  print("{} has {} members".format(csp.name, len(members)))
  for m in members:
    print("  {cid} - {fn} {sn}".format(cid=m.cid, fn=m.first_name, sn=m.surname))

API Reference
=============
This documentation is automatically generated from pyeactivities' source code.

.. autoclass:: pyeactivities.eactivities.EActivities

   .. automethod:: get_csps

.. autoclass:: pyeactivities.models.CSP

  .. automethod:: get_members

  .. automethod:: get_committee_members

  .. automethod:: get_online_sales

  .. automethod:: get_products

.. autoclass:: pyeactivities.models.Member

.. autoclass:: pyeactivities.models.CommitteeMember

.. autoclass:: pyeactivities.models.Customer

.. autoclass:: pyeactivities.models.VAT

.. autoclass:: pyeactivities.models.OnlineSale

.. autoclass:: pyeactivities.models.Account

.. autoclass:: pyeactivities.models.Activity

.. autoclass:: pyeactivities.models.ProductLine

.. autoclass:: pyeactivities.models.Product

  .. automethod:: get_sales

Exceptions
----------

.. automodule:: pyeactivities.exceptions
   :members:

Internal classes
----------------

.. autoclass:: pyeactivities.http.EActivitesClient


License
=======

pyeactivities is licensed under the `MIT License <https://opensource.org/licenses/MIT>`_

Copyright (c) 2019 Fraser May and Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
