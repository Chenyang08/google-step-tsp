#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:56:56 2018

@author: karry  (JIANG Nan)
"""

""" TSP using nearest neignbor heuristic and 2-opt algorithm
    works better for 64 <= n < 512 """


import math
import numpy as np


def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append([float(xy[0]), float(xy[1])])
        return cities


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def calPathDist(path):
    sum = 0.0
    for i in range(1, len(path)):
        sum += distance(cities[path[i]], cities[path[i-1]])
    return sum    


def pathCompare(path1, path2):
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False


def generateRandomPath(bestPath):
    a = np.random.randint(len(bestPath))
    while True:
        b = np.random.randint(len(bestPath))
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a+1]
    else:
        return a, b, bestPath[a:b+1]


def solve(cities):
    N = len(cities)
    
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    
    return tour


def reversePath(path):
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath


def updateBestPath(bestPath):
    count = 0
    while count < 3000:   # number of count (MaxCount)
        #print(calPathDist(bestPath))
        #print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        if pathCompare(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath


def opt2():
    bestPath = solve(cities)
    bestPath = np.append(bestPath, 0)
    bestPath = updateBestPath(bestPath)
    total_distance_bestPath = calPathDist(bestPath)
    #print(bestPath)
    print(total_distance_bestPath)
    return total_distance_bestPath


def trial(n):
    best_total_distance_bestPath = 10000000000000
    for i in range(n):
        total_distance_bestPath = opt2()
        if total_distance_bestPath < best_total_distance_bestPath:
            best_total_distance_bestPath = total_distance_bestPath
    print(best_total_distance_bestPath)


cities = read_input("input_5.csv")
n = 30
trial(n)

