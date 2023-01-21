import sys 
from time import perf_counter

result_list_loop = []
result_list_com = []

number_round = 10000000

print(sys.getsizeof(result_list_com), 'bytes')
# 56 bytes

start = perf_counter()
result_gen = (i*i for i in range(number_round))
print(perf_counter()-start)
# 1.79e-6 sec

print(sys.getsizeof(result_gen), 'bytes')
# 112 bytes

print(list(result_gen)[10])
# 100