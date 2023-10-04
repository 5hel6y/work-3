import random, time
sorrt = (random.sample(range(10000),1000))
sorrt_2 = (random.sample(range(10000),2000))
sorrt_3 = (random.sample(range(10000),5000))
sorrt_4 = (random.sample(range(10000),10000))

def bubble_sort(nums):
    start_time = time.time()
    swapped = bool
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]: # Меняем элементы местами
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    print(time.time() - start_time)


bubble_sort(sorrt)
bubble_sort(sorrt_2)
bubble_sort(sorrt_3)
bubble_sort(sorrt_4)
print(len(sorrt), len(sorrt_2), len(sorrt_3), len(sorrt_4))
#Результаты сортировки пузырьком дольше чем сортировка выборкой думаю это можно использовать при небольших сортировках