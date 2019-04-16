pyeactivities
=============

.. image:: https://img.shields.io/pypi/v/pyeactivities-ftm.svg
   :alt: PyPI
   :target: https://pypi.org/project/pyeactivities-ftm/

pyeactivities is a Python wrapper for the read-only API for eActivities, the
system provided by Imperial College Union for societies to manage themselves.

Installation
------------
To install pyeactivities, use ``pip``
::

  pip install pyeactivities-ftm

Usage
-----
To use pyeactivities you need the base URL for the API (found on Page 2 of the
API documentation), and your API key.

.. code-block:: python

  from pyeactivities.eactivities import EActivities

  # Base URL must end in trailing / (e.g. https://<eactivities>/API/)
  eactivities = EActivities(api_key, api_base_url)

  my_csp = eactivities.get_csps()[0]

  members = my_csp.get_members()

  print("{} has {} members".format(my_csp.name, len(members)))
  for m in members:
    print("  {cid} - {fn} {sn}".format(cid=m.cid, fn=m.first_name, sn=m.surname))


License
-------

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
