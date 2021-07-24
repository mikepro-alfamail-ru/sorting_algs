# Алгоритмы сортировки
from random import randint
import time

N = 400000
MASSIVE = [randint(0, N) for i in range(N)]


def insert_sort(massive: list):
    # Сортировка вставкой
    for i in range(1, N):
        key = massive[i]
        j = i - 1
        while j >= 0 and massive[j] > key:
            massive[j + 1] = massive[j]
            j -= 1
        massive[j + 1] = key
    return massive

def merge_sort(massive: list):
    # Сортировка слиянием

    def merge(massive1, massive2):
        out = []
        cur1, cur2 = 0, 0
        end1, end2 = len(massive1), len(massive2)

        while cur1 < end1 and cur2 < end2:
            if massive1[cur1] < massive2[cur2]:
                out.append(massive1[cur1])
                cur1 += 1
            else:
                out.append(massive2[cur2])
                cur2 += 1
        while cur1 < end1:
            out.append(massive1[cur1])
            cur1 += 1
        while cur2 < end2:
            out.append(massive2[cur2])
            cur2 += 1
        return out

    if len(massive) <= 1:
        return massive
    else:
        center = len(massive) // 2
        right = merge_sort(massive[0:center])
        left = merge_sort(massive[center:len(massive)])
        return merge(right, left)


def quick_sort(massive, start, end):

    def partition(massive, start, end):
        result = start
        for current in range(start, end - 1):
            if massive[current] <= massive[end -1]:
                massive[result], massive[current] = massive[current], massive[result]
                result += 1
        massive[result], massive[end - 1] = massive[end - 1], massive[result]
        return result

    if start >= end - 1:
        return
    else:
        center = partition(massive, start, end)
        quick_sort(massive, start, center)
        quick_sort(massive, center, end)
    return massive

def count_sort(massive):
    count_massive = [0 for i in range(len(massive) + 1)]
    for a in massive:
        count_massive[a] += 1

    index = 0
    for enum, a in enumerate(count_massive):
        for i in range(a):
            massive[index] = enum
            index += 1
    return massive


if __name__ == '__main__':
    # print(MASSIVE)
    # t0 = time.time()
    #
    # a = insert_sort(MASSIVE.copy())
    # t1 = time.time() - t0
    # print('insert - ', t1)
    # t0 = time.time()

    t0 = time.time()

    a = merge_sort(MASSIVE.copy())
    t1 = time.time() - t0
    print('merge - ', t1)
    # print(a)

    t0 = time.time()

    a = quick_sort(MASSIVE.copy(), 0, N)
    t1 = time.time() - t0
    print('quick - ', t1)
    # print(a)

    t0 = time.time()

    a = count_sort(MASSIVE.copy())

    t1 = time.time() - t0
    print('count - ', t1)
    # print(a)
