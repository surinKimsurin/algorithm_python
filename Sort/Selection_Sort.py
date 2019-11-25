'''
    선택정렬(Selection sort)의 기본 개념을 공부하도록한다.

    선택정렬은 현재 위치에 들어갈 값을 찾아 정렬하는 배열이다.
    오름차순 혹은 내림차순으로 현재 위치에 저장될 값의 크기와 다른 값을 비교하는 방식으로 진행된다.
    시간 복잡도는 O(N^2)
    공간복잡도는 하나의 배열에서 진행하기 때문에 O(N)
'''

# input : 1 10 5 8 6 4 3 2 9

def selection_sort(sort_list):
    total = len(sort_list)
    for i in range(0, total):
        for j in range(i+1, total):

            if sort_list[i] > sort_list[j]:
                tmp = sort_list[i]
                sort_list[i] = sort_list[j]
                sort_list[j] = tmp

    return sort_list


if __name__ == '__main__':
    sort_array = list(map(int, input().split(" ")))
    sorted_array = selection_sort(sort_array)

    print(sort_array)