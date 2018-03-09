# Real time crypto currency information
A program that displays crypto currency prices

User inputs a crypto currency symbol (BTC, ETH, ETC etc) 
Current price and other information related to the currency is printed as output.

The api used has a limit of 10 requests per minute
and performing an api request every time user requests slows down the program 
so a minimum interval is set between api requests 
when user requests for information between two information fetches,
information is printed to the user from the last fetch

Now checks for Internet connectivity before api request
If Internet connectivity is lost in midle, then works with last gained data until 
connection is established again.