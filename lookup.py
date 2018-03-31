from tkinter import * 
import requests
import json
import time
from tkinter import messagebox
############ global variables #####################
top10_crypto_list = []
last_time = float(0)
last_gui_update_time = 0
API_REQUEST_INTERVAL = 10
last_price = [float(0),float(0),float(0),float(0),float(0),float(0),float(0),float(0),float(0),float(0)]
###################################################


def display_message(message):
   messagebox.showinfo("Top 10 Crypto Currency List",message)




def get_top10_crypto_list():
	global last_time
	global top10_crypto_list
	if time.time() - last_time >= API_REQUEST_INTERVAL:
		try:
			api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=10")
			top10_crypto_list = json.loads(api_request.content.decode('utf-8'))

			# last_time variable is updated with current time when api request is done                                 
			# last_time is only updated when api request is successfull
			last_time =time.time()  
			print("updated") 
			return top10_crypto_list          
			
		except requests.ConnectionError:
			# last_time is 0 means no api request is not completed 
			# hence even if internet connection is lost after one or more api request
			# last updated list in variable api can be used
			if last_time ==0: 
				root = Tk()
				root.withdraw()   
				display_message("No Internet Access, Unable to display Information")                    
				exit(1)
			else:
				display_message("No Internet Access, Working Offline")
				return None


def set_change_color(value):
	if value >= 0:
		return "green"
	else: 
		return "red"


def set_price_color(old_value, new_value):
	if old_value == 0 :
		return "black"
	elif new_value > old_value: 
		return "green"
	elif new_value < old_value:
		return "red"


	
def default_gui():

	root.title("Top 10 Crypto Currency List")
	root.iconbitmap(r'BTC.ico')

	#################### CREATING HEADER ######################

	header_field = Label(root, text = "Name", bg = "white", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 0, sticky=N+S+E+W)

	header_field = Label(root, text = "Rank", bg = "silver", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 1, sticky=N+S+E+W)

	header_field = Label(root, text = "Price", bg = "white", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 2, sticky=N+S+E+W)

	header_field = Label(root, text = "1H Change", bg = "silver", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 3, sticky=N+S+E+W)

	header_field = Label(root, text = "24H Change", bg = "white", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 4, sticky=N+S+E+W)

	header_field = Label(root, text = "7 Day Change", bg = "silver", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 5, sticky=N+S+E+W)

	header_field = Label(root, text = "Market Cap", bg = "white", font ="Verdana 10 bold" )
	header_field.grid(row = 0, column = 6, sticky=N+S+E+W)

	######################### HEADER ENDS ########################



def update_gui_with(top10_crypto_list):	
	i = 1
	for coin in top10_crypto_list:

		name = coin["name"]
		rank = int(coin["rank"])
		price = float(coin["price_usd"])
		change_1h = float(coin["percent_change_1h"])
		change_24h = float(coin["percent_change_24h"])
		change_7d = float(coin["percent_change_7d"])
		market_cap = float(coin["market_cap_usd"])

		crypto_name_field = Label(root, text = name, bg = "white" )
		crypto_name_field.grid(row = i, column = 0, sticky=N+S+E+W)

		crypto_rank_field = Label(root, text = coin["rank"], bg = "silver" )
		crypto_rank_field.grid(row = i, column = 1, sticky=N+S+E+W)

		crypto_price_field = Label(root, text = "${0:.4f}".format(price), bg = "white", fg = set_price_color(last_price[i-1], price) )
		crypto_price_field.grid(row = i, column = 2, sticky=N+S+E+W)

		crypto_1h_change_field = Label(root, text = "{0:.2f}%".format(change_1h), bg = "silver", fg = set_change_color(change_1h) )
		crypto_1h_change_field.grid(row = i, column = 3, sticky=N+S+E+W)

		crypto_24h_change_field = Label(root, text = "{0:.2f}%".format(change_24h), bg = "white", fg = set_change_color(change_24h) )
		crypto_24h_change_field.grid(row = i, column = 4, sticky=N+S+E+W)

		crypto_7d_change_field = Label(root, text = "{0:.2f}%".format(change_7d), bg = "silver", fg = set_change_color(change_7d) )
		crypto_7d_change_field.grid(row = i, column = 5, sticky=N+S+E+W)		

		crypto_market_cap_field = Label(root, text = "${:0,.0f}".format(market_cap), bg = "white" )
		crypto_market_cap_field.grid(row = i, column = 6, sticky=N+S+E+W)	

		#print(i)
		last_price[i-1] = price

		i += 1
	

def update_gui():
	top10_crypto_list = get_top10_crypto_list()
	if not (top10_crypto_list is None):
		update_gui_with(top10_crypto_list)
	root.after(2000, update_gui)



top10_crypto_list = get_top10_crypto_list()
if not (top10_crypto_list is None):
	root = Tk()
	default_gui()
	update_gui_with(top10_crypto_list)
	update_gui()
	root.mainloop()
