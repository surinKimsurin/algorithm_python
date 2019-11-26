'''
    삽입 정렬(Insertion Sort)

    삽입정렬은 현재 위치에서 그 이하의 배열들을 비교해서 들어가야 할 위치를 찾아
    그 위치에 삽입하는 배열 알고리즘

    시간복잡도는 O(N^2)
    공간복잡도는 O(N)

'''


import time


def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

# input : 1 10 5 8 6 4 3 2 9
# input : 1 99 88 77 23 34 202 35 2 5 234 7 333 423 55
# input : 1 10 5 8 6 4 3 2 9
# input : 1 10 5 8 6 4 3 2 9

# input : 1 5 8 10 6 4 3 2 9

# 나의 풀이
@logging_time
def insertion_sort(sort_list):
    total = len(sort_list)
    for i in range(1, total):
        for j in range(0, i):
            if sort_list[i] < sort_list[j]:
                target_num = sort_list[i]
                for k in range(i, j, -1):
                    sort_list[k] = sort_list[k-1]
                sort_list[j] = target_num

    return sort_list


# 인터넷 풀이
@logging_time
def sel_sort(a):

    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

        return a


if __name__ == '__main__':
    sort_array = list(map(int, input().split(" ")))
    sorted_array = insertion_sort(sort_array)
    print(sorted_array)

    sorted_array2 = sel_sort(sort_array)
    print(sorted_array2)
