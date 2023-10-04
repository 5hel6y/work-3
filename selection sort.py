import random, time


def selection_sort(nsort):
    start_time = time.time() # время старта функции
    for i in range(len(nsort)):
        min_i = i
        for j in range(i + 1, len(nsort)):
            if nsort[min_i] > nsort[j]: min_i = j
        nsort[i], nsort[min_i] = nsort[min_i], nsort[i]
    print(time.time() - start_time) # время выполнения в секундах


sorrt = (random.sample(range(10000),1000))
sorrt_2 = (random.sample(range(10000),2000))
sorrt_3 = (random.sample(range(10000),5000))
sorrt_4 = (random.sample(range(10000),10000))
selection_sort(sorrt)
selection_sort(sorrt_2)
selection_sort(sorrt_3)
selection_sort(sorrt_4)
print(len(sorrt), len(sorrt_2), len(sorrt_3), len(sorrt_4))
# результаты при сортировки выборкой
