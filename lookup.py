import requests
import json
import os
import time

os.system('cls')
API_REQUEST_INTERVAL = 10       # time interval between two concicutive requests 
last_time = 0                   # initially set to 0
found = 0                       # initially set to 0 changes to 1 when given currency is found
#################################
while(True):
	# Accepting input from the user and a little sanitization is done
	currency = input("Enter Crypto Currency Symbol ; Eg: BTC for Bitcoin, XRP for Ripple etc : ")
	if currency.isalpha():
		currency = currency.upper()

		# Getting all the Crypto Information using Coinmarketcap api
		# The time interval between two api requests are limitted using API_REQUEST_INTERVAL variable 

		if time.time() - last_time >= API_REQUEST_INTERVAL:
			try:
				api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
				api = json.loads(api_request.content.decode('utf-8'))

				# last_time variable is updated with current time when api request is done                                 
				# last_time is only updated when api request is successfull
				last_time =time.time()             
				
			except requests.ConnectionError:
				# last_time is 0 means no api request is not completed 
				# hence even if internet connection is lost after one or more api request
				# last updated list in variable api can be used
				if last_time ==0:                         
					print(" No Internet Access, Unable to display Information")
					exit(1)
				else:
					print("\nNo Internet Access, Working Offline \n")

		# Looping through the list in api
		for x in api:
			# If currency input by user matches with value of dictionary item with key symbol, then 
			# information of that dictionary item is displayed
			if currency == x["symbol"]:
				found = 1        
				print("---------------------------------------")
				print("Crypto Currency: ",x["name"])
				print("Current Price: ${0:.4f}".format(float(x["price_usd"])))
				print("Rank: {0:.0f}".format(float(x["rank"])))
				print("Percent change in 1 hr: {0:.2f}%".format(float(x["percent_change_1h"])))
				print("Percent change in 1 day: {0:.2f}%".format(float(x["percent_change_24h"])))
				print("Percent change in 1 week: {0:.2f}%".format(float(x["percent_change_7d"])))
				print("Market Cap : ${0:.0f}".format(float(x["market_cap_usd"])))
				print("Volume (24h) : ${0:.0f}".format(float(x["24h_volume_usd"])))
				print("---------------------------------------")
		# if dictionary item not found invalid request message is displayed else found is again set to zero
		if found == 0: print("Invalid request please try again")
		else:
			found = 0            # found is set back to 0 again

	else:
		print("Enter symbol for a Crypto Currency like ETH, BTC, ETC, XRP, XLM, LTC etc")
	# Exit case from while loop when user input 0
	temp = input("Enter any key to continue, Enter 0 to exit ")
	if temp == '0': break

