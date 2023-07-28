#머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 
#피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이
# 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 
#return 하는 solution 함수를 완성해보세요.

#처음 문제는 라이브러리 안 쓰고 직접 작성하기

def solution(n):
    answer = 7
    count = 0
    while True:
        if n>answer:
            answer = answer+7
            count +=1
        else:
            count+=1
            break
    return count

#코드 줄이기
import math

def solution_2(n):
    answer = math.ceil(n/7)

    return answer


print(solution(15))
print(solution_2(15))