import numpy as np
from time import perf_counter

result_list_loop = []
result_list_com = []

number_round = 10000000

start = perf_counter()
for i in range(number_round):
  result_list_loop.append(i*i)
print(perf_counter()-start)
# 1.74 s

start = perf_counter()
result_list_com = [i*i for i in range(number_round)]
print(perf_counter()-start)
# 0.31 s

print(result_list_com[10])
# 100