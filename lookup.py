from tkinter import * 
import requests
import json
import os
os.system('cls')
#################################

root = Tk()


root.title("Crypto Currency Portfolio")
root.iconbitmap(r'BTC.ico')

#################### CREATING HEADER ######################
def pack_header(header):
	for field in header:
		header_field = Label(root, text = field, bg = ("white","silver")[bool(header.index(field)%2)], font ="Verdana 8 bold" )
		header_field.grid(row = 0, column = header.index(field), sticky=N+S+E+W)

header = ["Name", "Rank", "Price", "Change 1H", "Change 24H", "Change 1D", "Market Cap", "Total Paid" ,"Current","Profit/Loss"]

pack_header(header)

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

def pack_values(row,values_list):
	for value in values_list:
		values_field = Label(root, text = value, bg = ("white","silver")[bool(values_list.index(value)%2)], font ="Verdana 8 bold" )
		values_field.grid(row = row, column = values_list.index(value), sticky=N+S+E+W)





def lookup():

	api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
	api = json.loads(api_request.content.decode('utf-8'))
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
		}
	]
	portfolio_profit_loss = 0
	i = 1
	for x in api:
		for coin in my_portfolio:
			if coin["symbol"] == x["symbol"]:

				total_paid = coin["amount_owned"] * coin["price_paid_per_coin_usd"]
				current_value = coin["amount_owned"] * float(x["price_usd"])
				profit_loss = current_value - total_paid
				portfolio_profit_loss += profit_loss
				profit_loss_per_coin = float(x["price_usd"]) - coin["price_paid_per_coin_usd"]

				values_list = [x["name"], x["rank"], x["price_usd"], x["percent_change_1h"], x["percent_change_24h"]]
				values_list.extend([x["percent_change_7d"], x["market_cap_usd"], "${0:.0f}".format(float(total_paid))]) 
				values_list.extend(["${0:.0f}".format(float(current_value)), "${0:.4f}".format(float(profit_loss_per_coin))])
				pack_values(i,values_list)
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