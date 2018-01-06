from data_frame import get_self_made_data_frame
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot

start_date = '2012-01-01'
end_date = '2012-09-30'

# get stock data frame
stock_frame = get_self_made_data_frame('IBM', start_date, end_date)

# get volatility and stock value
stock_frame = stock_frame.loc[:,['Adj Close', 'volatility']]

#plot
stock_frame.plot(subplots=True)
plt.legend(loc='upper left')
plt.show()