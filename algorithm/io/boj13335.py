from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0 for _ in range(w)])
time = 0

while trucks:
    bridge.popleft()
    if len(bridge) < w :
        if sum(bridge) + trucks[0] <= L:
            truck = trucks.pop(0)
            bridge.append(truck)
        else :
            bridge.append(0)
    time += 1 
time += w 
print(time)