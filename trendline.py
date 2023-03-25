#! /usr/bin/python3


"""Trend Lines detection module"""

from pandas import DataFrame
from format import ohlc_data
from pattern_recognition import important_points_recognition_vert


def are_aligned(data: DataFrame, index_list: list):
    prices_list = [data['Close'][i] for i in index_list]
    points = DataFrame(index_list, prices_list)
    print(points)


if __name__ == "__main__":
    hist = ohlc_data("EURUSD", "2023-01-01")
    are_aligned(hist, [0, 13, 18, 27, 45])