import time
import matplotlib.pyplot as plt

elementos = [['a', 'b', 'c', 'd'],['q', 'i', 'n', 'm'],['f', 'e', 'h', 'j'],['p', 'o', 'l','g']]
lista1 = []
for sublista1 in elementos:
    for item in sublista1:
        lista1.append(item)

for i in range(len(lista1)):
    for j in range(len(lista1)-1-i):
        if lista1[j] > lista1[j+1]:
            lista1[j], lista1[j+1] = lista1[j+1], lista1[j]

print("crescente:", lista1)

for i in range(len(lista1)):
    for j in range(len(lista1)-1-i):
        if lista1[j] < lista1[j+1]:
            lista1[j], lista1[j+1] = lista1[j+1], lista1[j]

print("decrescente:", lista1)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

ns = []
tempos = []

for n in range(1, 16):
    start = time.perf_counter()
    result= fib(n)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    ns.append(n)
    tempos.append(ms)
print(result) 

plt.plot(ns, tempos)
plt.xlabel('Valor de n')
plt.ylabel('Tempo de execução (micro segundos)')
plt.show()