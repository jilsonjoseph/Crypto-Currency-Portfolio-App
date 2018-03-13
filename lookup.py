import requests
import json
import os
os.system('cls')
#################################


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

for x in api:
	for coin in my_portfolio:
		if coin["symbol"] == x["symbol"]:

			total_paid = coin["amount_owned"] * coin["price_paid_per_coin_usd"]
			current_value = coin["amount_owned"] * float(x["price_usd"])
			profit_loss = current_value - total_paid
			portfolio_profit_loss += profit_loss
			profit_loss_per_coin = float(x["price_usd"]) - coin["price_paid_per_coin_usd"]

			print("---------------------")
			print(x["name"])
			print(" ${0:.4f}".format(float(x["price_usd"])))
			print(" Rank {0:.0f}".format(float(x["rank"])))
			
			print(" Price payed per coin ${0:.4f}".format(float(coin["price_paid_per_coin_usd"])))
			print(" Total Paid ${0:.0f}".format(float(total_paid)))
			print(" Current Value ${0:.0f}".format(float(current_value)))
			print(" Profit/Loss ${0:.0f}".format(float(profit_loss)))
			print(" Profit/Loss per coin {0:.4f}".format(float(profit_loss_per_coin)))
			print("---------------------")

print("Portfolio Profit/Loss: ${0:.2f}".format(float(portfolio_profit_loss)))