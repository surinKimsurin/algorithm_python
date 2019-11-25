'''
    삽입 정렬(Insertion Sort)

    삽입정렬은 현재 위치에서 그 이하의 배열들을 비교해서 들어가야 할 위치를 찾아
    그 위치에 삽입하는 배열 알고리즘

    시간복잡도는 O(N^2)
    공간복잡도는 O(N)

'''

# input : 1 10 5 8 6 4 3 2 9


def insertion_sort(sort_list):
    # total = len(sort_list)
    # for i in range(1, total):
    #     for j in range(0, i):
    #         if sort_list[i] < sort_list[j]:


if __name__ == '__main__':
    sort_array = list(map(int, input().split(" ")))
    sorted_array = insertion_sort(sort_array)
    print("")