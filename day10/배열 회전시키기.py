# 배열 회전시키기

# 문제설명
#정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다.
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을
# return하도록 solution 함수를 완성해주세요.

# 입출력 예 1
numbers = [1,2,3]
direction = "right"

# 입출력 예 2
# numbers = [4, 455, 6, 4, -1, 45, 6]
# direction = "left"

temp = 0

def solution(numbers,direction):
    if 'right'==direction:
        numbers.insert(0,numbers[-1])
        numbers.pop()
        return numbers
    elif 'left'==direction:
        numbers.append(numbers[0])
        numbers.pop(0)
        return numbers

print(solution(numbers,direction))