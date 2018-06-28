import sys
import math

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def init(cities):
    N = len(cities)
    INF = 999999
    dp = [[0] * N for i in range(1 << N)]
    path = [[0] * N for i in range(1 << N)]
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j]) #计算城市之间的距离

    for i in range(1 << N):
        for j in range(N):
            dp[i][j] = INF
            path[i][j] = []#初始化，除了dp[1][0]，其余值都为INF
    return dist, dp, path

def solve(cities):
    N = len(cities)
    M = (1 << N)
    dist, dp, path = init(cities)
    dp[1][0] = 0
    path[1][0].append(0)
    for i in range(M):
        for j in range(N):
            if (i & (1 << j)):
                continue
            for k in range(N):
                if (i & (1 << k)):
                    if (dp[i][k] + dist[k][j] < dp[(1 << j) | i][j]):
                        dp[(1 << j) | i][j] = dp[i][k] + dist[k][j]
                        path[(1 << j) | i][j] = path[i][k]
                        path[(1 << j) | i][j].append(j)
                    dp[(1 << j) | i][j] = min(dp[(1 << j) | i][j], dp[i][k] + dist[k][j])
    for i in range(N):
        ans = dp[M - 1][i] + dist[i][0]
        tour = path[M-1][i]
    print(ans)
    return tour

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)