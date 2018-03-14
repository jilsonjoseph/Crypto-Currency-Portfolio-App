from tkinter import * 
import requests
import json
import os
os.system('cls')
#################################

root = Tk()

def change_color(value):
	if value >= 0:
		return "green"
	else: 
		return "red"


root.title("Crypto Currency Portfolio")
root.iconbitmap(r'BTC.ico')

#################### CREATING HEADER ######################
#def pack_header(header):
#	for field in header:
#		i = 0
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

header_field = Label(root, text = "1Day Change", bg = "silver", font ="Verdana 10 bold" )
header_field.grid(row = 0, column = 5, sticky=N+S+E+W)

header_field = Label(root, text = "Market Cap", bg = "white", font ="Verdana 10 bold" )
header_field.grid(row = 0, column = 6, sticky=N+S+E+W)
#		i += 1

#header = ["Name", "Rank", "Price", "Change 1H", "Change 24H", "Change 1D", "Market Cap"]

#pack_header(header)

#pack_to_header("Name", 0, "white")
#pack_to_header("Rank", 1, "silver")
#pack_to_header("Price", 2, "white")
#pack_to_header("Change 1H", 3, "silver")
#pack_to_header("Change 24H", 4, "white")
#pack_to_header("Change 1D", 5, "silver")
#pack_to_header("Market Cap", 6, "white")
#pack_to_header("Total Paid", 7, "silver")
#pack_to_header("Current", 8, "white")
#pack_to_header("Profit/Loss", 9, "silver")

################### END OF HEADER ##########################

#def pack_values(row,values_list):
#	for value in values_list:
#		values_field = Label(root, text = value, bg = ("white","silver")[bool(i%2)] )
#		values_field.grid(row = row, column = values_list.index(value), sticky=N+S+E+W)
#		i += 1





def lookup():

#	def get_crypto_info_list():
	api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
	crypto_info_list = json.loads(api_request.content.decode('utf-8'))

#	get_crypto_info_list()
	# My Portfolio
	my_portfolio = [
		{
			"symbol": "BTC",
			"amount_owned": 10,
			"price_paid_per_coin_usd": 8000,
		},

		{
			"symbol": "ETH",
			"amount_owned": 100,
			"price_paid_per_coin_usd": 300,
		},

		{
			"symbol": "XRP",
			"amount_owned": 1000,
			"price_paid_per_coin_usd": .8,
		},

		{
			"symbol": "XLM",
			"amount_owned": 1000,
			"price_paid_per_coin_usd": .8,
		},

		{
			"symbol": "NEO",
			"amount_owned": 1000,
			"price_paid_per_coin_usd": .8,
		},

		{
			"symbol": "DASH",
			"amount_owned": 1000,
			"price_paid_per_coin_usd": .8,
		}
	]
	portfolio_profit_loss = 0
	i = 1
	for coin in crypto_info_list:
		for my_coin in my_portfolio:
			if my_coin["symbol"] == coin["symbol"]:

				name = coin["name"]
				rank = int(coin["rank"])
				price = float(coin["price_usd"])
				change_1h = float(coin["percent_change_1h"])
				change_24h = float(coin["percent_change_24h"])
				change_7d = float(coin["percent_change_7d"])
				market_cap = coin["market_cap_usd"]




				#total_paid = coin["amount_owned"] * coin["price_paid_per_coin_usd"]
				#current_value = coin["amount_owned"] * float(x["price_usd"])
				#profit_loss = current_value - total_paid
				#portfolio_profit_loss += profit_loss
				#profit_loss_per_coin = float(x["price_usd"]) - coin["price_paid_per_coin_usd"]

				#values_list = [name, rank, "${0:.4f}".format(price), "{0:.2f}%".format(change_1h),"{0:.2f}%".format(change_24h), "{0:.2f}%".format(change_7d), market_cap]
				#values_list.extend(["${0:.0f}".format(float(total_paid)), "${0:.0f}".format(float(current_value)), "${0:.4f}".format(float(profit_loss_per_coin))])
				#pack_values(i,values_list)
				#i += 1

				values_field = Label(root, text = name, bg = "white" )
				values_field.grid(row = i, column = 0, sticky=N+S+E+W)

				values_field = Label(root, text = coin["rank"], bg = "silver" )
				values_field.grid(row = i, column = 1, sticky=N+S+E+W)

				values_field = Label(root, text = "${0:.4f}".format(price), bg = "white" )
				values_field.grid(row = i, column = 2, sticky=N+S+E+W)

				values_field = Label(root, text = "{0:.2f}%".format(change_1h), bg = "silver", fg = change_color(change_1h) )
				values_field.grid(row = i, column = 3, sticky=N+S+E+W)

				values_field = Label(root, text = "{0:.2f}%".format(change_24h), bg = "white", fg = change_color(change_24h) )
				values_field.grid(row = i, column = 4, sticky=N+S+E+W)

				values_field = Label(root, text = "{0:.2f}%".format(change_7d), bg = "silver", fg = change_color(change_7d) )
				values_field.grid(row = i, column = 5, sticky=N+S+E+W)

				values_field = Label(root, text = market_cap, bg = "white" )
				values_field.grid(row = i, column = 6, sticky=N+S+E+W)		

				i += 1		

				#print("---------------------")
				#print(x["name"])
				#print(" ${0:.4f}".format(float(x["price_usd"])))
				#print(" Rank {0:.0f}".format(float(x["rank"])))
				
				#print(" Price payed per coin ${0:.4f}".format(float(coin["price_paid_per_coin_usd"])))
				#print(" Total Paid ${0:.0f}".format(float(total_paid)))
				#print(" Current Value ${0:.0f}".format(float(current_value)))
				#print(" Profit/Loss ${0:.0f}".format(float(profit_loss)))
				#print(" Profit/Loss per coin {0:.4f}".format(float(profit_loss_per_coin)))
				#print("---------------------")

	print("Portfolio Profit/Loss: ${0:.2f}".format(float(portfolio_profit_loss)))
lookup()

root.mainloop()