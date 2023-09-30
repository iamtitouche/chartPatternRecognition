#! /usr/bin/python3


"""Data format module"""


import yfinance as yf


def ohlc_data(symbol: str, start: str, timeframe="1h",):
    """Returns the ohlc data of symbol in the timeframe wanted from a specific start date.

    Args:
        symbol (str): symbol name
        start (str): start date - format "AAAA-MM-DD"
        timeframe (str, optional): timeframe of the data. Defaults to "1d".
    
    Returns:
        pandas.Dataframe : dataframe containing the requested ohlc data
    """
    ticker = yf.Ticker(ticker=symbol)
    history = ticker.history(period=timeframe, start=start)
    useless_infos = ["Volume", "Dividends", "Stock Splits"]
    for info in useless_infos:
        if info in history.keys():
            history = history.drop(labels=[info], axis=1)
    return history


if __name__ == "__main__":
    hist = ohlc_data("AMZN", "2023-01-01")
    print(hist)
    print(len(hist))
