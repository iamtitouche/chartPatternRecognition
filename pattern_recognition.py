#! /usr/bin/python3


"""Swings highs and lows detection module"""


from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


def swings_detection(data, order: int):
    """_summary_

    Args:
        data (_type_): _description_
        order (int): _description_

    Returns:
        _type_: _description_
    """
    lows_indexes = swing_low(data, order)
    highs_indexes = swing_high(data, order)

    swings = {}
    swings["swing_lows"] = lows_indexes
    swings["swing_highs"] = highs_indexes

    return swings



def swing_low(data, order: int):
    """_summary_

    Args:
        data (_type_): _description_
        order (int): _description_

    Returns:
        _type_: _description_
    """
    swing_lows_indexes = []
    shifts = [i for i in range(-order, 0)] + [i for i in range(1, order + 1)]
    for i in range(order, len(data) - 1 - order):
        for j in shifts:
            if data[i + j, 2] < data[i, 2]:
                break
            if j == shifts[-1]:
                swing_lows_indexes.append(i)
    return swing_lows_indexes

def swing_high(data, order: int):
    """_summary_

    Args:
        data (_type_): _description_
        order (int): _description_

    Returns:
        _type_: _description_
    """
    swing_highs_indexes = []
    shifts = [i for i in range(-order, 0)] + [i for i in range(1, order + 1)]
    for i in range(order, len(data) - 1 - order):
        for j in shifts:
            if data[i + j, 1] > data[i, 1]:
                break
            if j == shifts[-1]:
                swing_highs_indexes.append(i)
    return swing_highs_indexes

def important_points_recogn_vert(data, n_points: int):
    """_summary_

    Args:
        data (_type_): _description_
        n_points (int): _description_

    Returns:
        _type_: _description_
    """
    important_points_indexes = [0, len(data)- 1]

    a_1 = (data[-1] - data[0]) / (len(data)-1)
    a_2 = data[0]

    trend_line = [a_1 * i + a_2 for i in range(len(data))]
    print(trend_line)
    distance = [abs(data[i] - trend_line[i]) for i in range(len(data))]
    print(distance)
    for _ in range(n_points - 2):
        new_point_index = 1
        max_distance = distance[1]
        for i in range(1, len(data) - 1):
            if distance[i] > max_distance:
                if i not in important_points_indexes:
                    new_point_index = i
                    max_distance = distance[i]
        important_points_indexes.append(new_point_index)
        important_points_indexes.sort()
        for i in range(len(important_points_indexes)-1):
            start, end = important_points_indexes[i], important_points_indexes[i+1]
            a_1 = (data[end] - data[start]) / (end - start)
            a_2 = data[start] - a_1 * start
            trend_line[start:end] = [a_1 * j + a_2 for j in range(start, end)]
        print(trend_line)
        distance = [abs(data[i] - trend_line[i]) for i in range(len(data))]

    return important_points_indexes

def important_points_recognition_perp(data, n_points: int):
    """_summary_

    Args:
        data (_type_): _description_
        n_points (int): _description_

    Returns:
        _type_: _description_
    """
    important_points_indexes = [0, len(data)- 1]
    a_1 = (data[-1] - data[0]) / (len(data)-1)
    a_2 = data[0]
    distance = [abs(a_1 * i - data[i] + a_2) / (a_1**2 + 1) ** (1/2) for i in range(len(data))]
    for _ in range(n_points - 2):
        new_point_index = 1
        max_distance = distance[1]
        for i in range(1, len(data) - 1):
            if distance[i] > max_distance:
                if i not in important_points_indexes:
                    new_point_index = i
                    max_distance = distance[i]
        important_points_indexes.append(new_point_index)
        important_points_indexes.sort()
        for i in range(len(important_points_indexes)-1):
            start, end = important_points_indexes[i], important_points_indexes[i+1]
            a_1 = (data[end] - data[start]) / (end - start)
            a_2 = data[start] - a_1 * start
            for i in range(start, end):
                distance[i] = abs(a_1 * i - data[i] + a_2) / (a_1**2 + 1) ** (1/2)
    return important_points_indexes

def important_points_recogn_perc_diff(data, max_diff = 5):
    """_summary_

    Args:
        data (_type_): _description_
        max_diff (int, optional): _description_. Defaults to 5.

    Returns:
        _type_: _description_
    """
    important_points_indexes = [0, len(data)- 1]
    a_1 = (data[-1] - data[0]) / (len(data)-1)
    a_2 = data[0]
    trend_line = [a_1 * i + a_2 for i in range(len(data))]
    print(trend_line)
    distance = [abs(data[i] - trend_line[i]) for i in range(len(data))]
    print(distance)
    diff = [100 * distance[i] / trend_line[i] for i in range(len(data))]
    while max(diff) > max_diff:
        new_point_index = 1
        max_distance = distance[1]
        for i in range(1, len(data) - 1):
            if distance[i] > max_distance:
                if i not in important_points_indexes:
                    new_point_index = i
                    max_distance = distance[i]
        important_points_indexes.append(new_point_index)
        important_points_indexes.sort()
        for i in range(len(important_points_indexes)-1):
            start, end = important_points_indexes[i], important_points_indexes[i+1]
            a_1 = (data[end] - data[start]) / (end - start)
            a_2 = data[start] - a_1 * start
            trend_line[start:end] = [a_1 * j + a_2 for j in range(start, end)]
        print(trend_line)
        distance = [abs(data[i] - trend_line[i]) for i in range(len(data))]
        diff = [100 * distance[i] / trend_line[i] for i in range(len(data))]
    return important_points_indexes
