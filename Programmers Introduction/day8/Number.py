# 순서쌍의 개수

#문제 설명
#순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])
    return len(answer) 

# 참고로 extend()함수는 복수의 오브젝트를 합쳐서(merge)로 되돌려 주는 함수이다.