# 짝수의 합

# 문제 설명
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 
# return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# 0 < n ≤ 1000

# 입출력 예
# n : 10
# result : 30

# 구현

sum =0
for i in range(11): 
    if i%2==0 :
         sum+=i
print(sum)

# 정답
def solution(n):
    sum = 0 
    for i in range(n+1): 
        if i%2==0 :
            sum+=i
    return sum

# 간출이자
def solution(n): return sum([i for i in range(2,n+1,2)])