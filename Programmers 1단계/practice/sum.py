# 약수의 합

#문제 설명
#정수 n을 입력받아 n의 약수를 모두 더한 값을
# 리턴하는 함수, solution을 완성해주세요.

n = 12
number_sum = 0
for i in range(1,n+1):
    if n%i==0:
        number_sum+=i

print(number_sum)

# 코드를 줄여보자

def sumDivisor(num):
    return sum([i for i in range(1,num+1) if num%i==0])

print(sumDivisor(12))
