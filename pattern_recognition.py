import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import yfinance

entry = yfinance.Ticker('GBPUSD=X').history(period='1m', start ='2023-03-01')
entry = list(entry['Close'])
plt.plot(entry)

def importantPointsRecogn(data, n_points: int):
    important_points_indexes = [0, len(data)- 1]

    a = (data[-1] - data[0]) / (len(data)-1)
    b = data[0]

    trend_line = [a * i + b for i in range(len(data))]
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
            a = (data[end] - data[start]) / (end - start)
            b = data[start] - a * start
            trend_line[start:end] = [a * j + b for j in range(start, end)]
        print(trend_line)
        distance = [abs(data[i] - trend_line[i]) for i in range(len(data))]

    return important_points_indexes



def importantPointsRecogn2(data, max_diff = 5):
    important_points_indexes = [0, len(data)- 1]

    a = (data[-1] - data[0]) / (len(data)-1)
    b = data[0]

    trend_line = [a * i + b for i in range(len(data))]
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
            a = (data[end] - data[start]) / (end - start)
            b = data[start] - a * start
            trend_line[start:end] = [a * j + b for j in range(start, end)]
        print(trend_line)
        distance = [abs(data[i] - trend_line[i]) for i in range(len(data))]
        diff = [100 * distance[i] / trend_line[i] for i in range(len(data))]

    return important_points_indexes

res = importantPointsRecogn2(entry, 1.4)

new_data = [entry[i] for i in res]

plt.plot(res, new_data, c='red')

res = importantPointsRecogn2(entry, 0.7)

new_data = [entry[i] for i in res]
plt.plot(res, new_data, c='green')
plt.show()

