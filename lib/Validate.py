'''
' Author(s): Mathew Norman
' Date created: 10/04/18
' Description: 
'  Simulates a card validation
'''

import requests

class Validate:

	def card(self, id, signature):
		response = False
		r = requests.get("http://therfid.men/php/reader/approve.php?reader=" + signature)
		if (r.text == "1"):
                        a = requests.get("http://therfid.men/php/reader/authenticate.php?reader=" + signature + "&key=" + str(id))
                        if (a.text == "1"):
                                response = True
		return response