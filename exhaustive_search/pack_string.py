# 완전 탐색이란 가능한 경우의 수를 일일이 나열하면서 답을 찾는 방법

# 카카오 문제 있는 블로그
# https://blog.naver.com/gngh0101/221725205795

# 완전 탐색 문제들 선별해놓은 블로그
# https://brenden.tistory.com/10

import ast
import math

'''
    chunk한 값을 비교해서 배열에 넣구
    값의 길이를 비교한다.
'''

input_string = ast.literal_eval(input())
length = math.ceil(len(input_string)/2)+1
total_list_text = []


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]


def get_yaksoo(total_length):
    length_list = []
    for num in range(1, total_length):
        if total_length % num == 0:
            length_list.append(num)

    return length_list


def get_pack_length(input_string, num, total_list):
    split_string = list(chunks(input_string, num))
    now_chunk = None
    now_chunk_count = 1

    for idx, chunk_string in enumerate(split_string):
        # 현재랑 이전 chunk가 같으면 +1
        if chunk_string == now_chunk:
            now_chunk_count += 1

        else:
            # 처음인 경우
            if idx == 0:
                now_chunk = chunk_string
                continue

            # 처음 마지막이 아니면서 현재랑 이전이 달라지면
            else:
                total_list.append(str(now_chunk_count) + now_chunk)
                now_chunk = chunk_string
                now_chunk_count = 1

        # 마지막인 경우
        if idx == len(split_string) - 1:
            total_list.append(str(now_chunk_count) + chunk_string)
            total_list_text.append("".join(total_list).replace("1", ""))


if __name__ == '__main__':
    total_length = len(input_string)
    num_list = get_yaksoo(total_length)

    for num in range(1, length):
        get_pack_length(input_string, num, [])

    print(len(min(list(set(total_list_text)), key=len)))