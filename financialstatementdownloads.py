import yfinance as yf

ticker = "JPM"

stock = yf.Ticker(ticker)

financials = stock.financials
balance_sheet = stock.balance_sheet  
cash_flow = stock.cashflow  

financials.to_csv("income_statement.csv")
balance_sheet.to_csv("balance_sheet.csv")
cash_flow.to_csv("cash_flow.csv")

print("Files saved!")
