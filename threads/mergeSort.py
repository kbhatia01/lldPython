import concurrent.futures
import random
import time


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)


def merge(leftarr, rightarr):
    result = []
    left = 0
    right = 0

    while left < len(leftarr) and right < len(rightarr):
        if leftarr[left] <= rightarr[right]:
            result.append(leftarr[left])
            left += 1
        else:
            result.append(rightarr[right])
            right += 1
    result.extend(leftarr[left:])
    result.extend(rightarr[right:])
    return result


def parllel_merge_sort(arr, maxWorkers):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    with concurrent.futures.ProcessPoolExecutor(max_workers=maxWorkers) as executor:
        left_future = executor.submit(mergeSort, left)
        right_future = executor.submit(mergeSort, right)

        left_arr = left_future.result()
        right_arr = right_future.result()

    return  merge(left_arr, right_arr)


if __name__ == "__main__":
    arr = [random.randint(0, 100) for i in range(5000000)]

    # Single-threaded merge sort
    start_time = time.time()
    sorted_array_single_thread = mergeSort(arr)
    end_time = time.time()
    single_thread_duration = end_time - start_time

    print(f"Execution time: {end_time - start_time}")

    # print(f"Single-threaded sorted array: {sorted_array_single_thread}")
    start_time = time.time()

    max_workers = 4
    sorted_arr = parllel_merge_sort(arr, max_workers)
    # print(sorted_arr)
    end_time = time.time()

    print(f"Execution time: {end_time - start_time}")
