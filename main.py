import time


def counting_sort(v):
    h = len(v)
    resultado = [0] * h
    count = [0] * 10

    for i in range(0, h):
        count[v[i]] += 1

    for j in range(1,10):
        count[j] += count[j-1]

    a = h-1
    while a >= 0:
        resultado[count[v[a]]-1] = v[a]
        count[v[a]] -= 1
        a -= 1

    for k in range(0, h):
        v[k] = resultado[k]

v1 = [4,2,2,8,3,3,1]
antes = time.time()
print("Vetor desordenado")
print(v1,"\n")
counting_sort(v1)
depois = time.time()
total = (depois-antes) * 1000
print("Vetor ordenado com o algorítimo Counting Sort")
print(v1)

print("tempo de execução %0.2fms" % total)