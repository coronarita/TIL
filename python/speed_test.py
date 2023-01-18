import numpy as np
from time import perf_counter

result_list = []
company_list = ["Samsung", "LG", "Google", "Apple", "Alibaba"]
company_list_sample = np.repeat(company_list, 10**7)

start = perf_counter()
for company in company_list_sample:
  result_list.append(company.lower())
print(perf_counter()-start)
# 12.17 s

start = perf_counter()
result_list = map(str.lower, company_list_sample)
print(perf_counter()-start)
# 0.87 s
