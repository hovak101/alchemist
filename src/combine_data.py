import yfinance as yf
data = yf.download("AMZN, HD, COST, BURL, ULTA, WMT, BBY, TGT")
print(data.shape)
print(data.info())