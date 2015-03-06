#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html
import requests

# Vilken basadress vill vi kolla på? I det här fallet är det tre sidor med nummer.
base_url = 'http://iogt.se/employee/page/'

# Tom lista att fylla med anställda
employees = []


# Loopa igenom de tre sidorna med anställda
for counter in [1,2,3]:
	url_string = base_url + str(counter) +'/'
	print url_string
	page = requests.get(url_string)
	tree = html.fromstring(page.text)

	# Fyll på listan med namnen (som står vid en h2-tagg)
	employees += tree.xpath('//h2/text()')

# Skriv ut listan (oformaterat)
print employees

# Skriv ut antalet anställda (som är samma som längden på listan)
print 'Antal: ' + str(len(employees))