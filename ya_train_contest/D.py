from itertools import pairwise


def new_mayor(k: int, n: int, m: int):
    repairs = [[int(num) for num in input().split()] for _ in range(n)]
    
    roads_repair = {}
    for day, road in repairs:
        roads_repair[road] = roads_repair.get(road, []) + [day]
    if len(roads_repair) > m:
        return -1
    
    m_left = m - len(roads_repair)
    unhappy_points = {}
    for road, days_started in roads_repair.items():
        days_started.sort()
        
        for a, b in pairwise(days_started):
            unhappy_points[b - a] = unhappy_points.get(b - a, []) + [road]
    
    for point in sorted(unhappy_points.keys(), reverse=True):
        if m_left == 0:
            break
        for _ in zip(range(m_left), unhappy_points[point]):
            unhappy_points[point].pop()
            
    
    res = 0
    for point, roads in unhappy_points.items():
        res += point * len(roads)
    
    return res


print(new_mayor(*[int(num) for num in input().split()]))
