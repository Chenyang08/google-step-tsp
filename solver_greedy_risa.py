#!/usr/bin/env python3

import sys
import math
import random

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def greedy(cities):
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

def random_choose(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = random.sample(unvisited_cities, 1)[0]
        # next_city = min(unvisited_cities,
                        # key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour


def opt_2(tour, cities):
    for i in range(100000):
        point1 = int(random.uniform(1, len(tour)))
        point2 = int(random.uniform(1, len(tour)))
        while point2 == point1:
            point2 = int(random.uniform(1, len(tour)))
        orig = cal_dist(tour, cities)
        tour[point1], tour[point2] = tour[point2], tour[point1]
        updated = cal_dist(tour, cities)
        if orig < updated:
            tour[point1], tour[point2] = tour[point2], tour[point1]
    return tour


def opt_2_optimal(tour, cities):
    flag = True
    while flag:
        flag = False
        for i in range(len(tour)):
            for j in range(len(tour)):
                # print(i,j)
                orig = cal_dist(tour, cities)
                tour[i], tour[j] = tour[j], tour[i]
                updated = cal_dist(tour, cities)
                if orig <= updated:
                    tour[i], tour[j] = tour[j], tour[i]
                else:
                    flag = True
                    break
            if flag:
                break
    return tour



def cal_dist(tour, cities):
    dist = 0 
    for i in range(len(tour)-1):
    # for i in range(tour-1):
        dist += distance(cities[tour[i]], cities[tour[i+1]])
    dist += distance(cities[tour[len(tour)-1]], cities[0])
    return dist


if __name__ == '__main__':
    assert len(sys.argv) > 1
    # tmp_tour = greedy(read_input(sys.argv[1]))
    tmp_tour = random_choose(read_input(sys.argv[1]))
    tour = opt_2_optimal(tmp_tour[:], read_input(sys.argv[1]))
    print_tour(tour)
    # print(cal_dist(tour, read_input(sys.argv[1])))