import random
sorrt = (random.sample(range(10000),1000))
sorrt_2 = (random.sample(range(10000),2000))
sorrt_3 = (random.sample(range(10000),5000))
sorrt_4 = (random.sample(range(10000),10000))


def arifmetic_sort(left, right):
    left_position = right_position = 0
    sorted_list = []
    left_len = len(left)
    right_len = len(right)
    for asort in range(left_len+right_len):
        if left_position < left_len and right_position < right_len:
            if left[left_position] <= right[right_position]:
                sorted_list.append(left[left_position])
                left_position += 1
            else:
                sorted_list.append(right[right_position])
                right_position += 1
        elif  left_position == left_len:
            sorted_list.append(right[right_position])
            right_position += 1
        elif right_position == right_len:
            sorted_list.append((left[left_position]))
            left_position += 1
    return sorted_list


def ar_sort(liste):
    if len(liste) <= 1:
        return liste
    miidle = len(liste) // 2
    left = ar_sort(liste[:miidle])
    right = ar_sort(liste[miidle:])
    return arifmetic_sort(left, right)


sorrt = ar_sort(sorrt)
print(sorrt)