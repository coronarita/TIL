n = int(input())

fibo_list = [0, 1]+ [0]* 47
# print(fibo_list)

def fibo(n):
    for i in range(2, n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[n]

print(fibo(n))