import yfinance as yf
import matplotlib.pyplot as plt

def assess_dead_cat_bounce(ticker_symbol):
    # Fetch historical stock data
    stock_data = yf.download(ticker_symbol, start='2023-01-01', end='2024-01-01')

    # Calculate percentage change in closing prices
    stock_data['Price Change'] = stock_data['Close'].pct_change() * 100

    # Plot the closing prices and percentage change
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(stock_data['Close'])
    plt.title(f'{ticker_symbol} Closing Prices')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.bar(stock_data.index, stock_data['Price Change'], color='red' if stock_data['Price Change'].iloc[-1] < 0 else 'green')
    plt.title(f'{ticker_symbol} Percentage Change')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Assess for a dead cat bounce
    last_price_change = stock_data['Price Change'].iloc[-1]
    if last_price_change > 0 and stock_data['Price Change'].iloc[-2] < 0:
        print(f'{ticker_symbol} shows signs of a potential dead cat bounce.')
    else:
        print(f'{ticker_symbol} does not show clear signs of a dead cat bounce.')
