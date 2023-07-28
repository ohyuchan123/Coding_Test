# 문자 반복 출력하기

#문제 설명
#문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을
# return 하도록 solution 함수를 완성해보세요.

a = "hello"
n = 3
d = ''
for i in range(len(a)):
    d = d + a[i]*n
print(d)

# 함수 구현
def solution(my_string, n):
    d = ''
    for i in range(len(my_string)):
        d = d + my_string[i]*n
    return d

# 또 다른 방법
def solution_2(my_string,n):
    return ''.join(i*n for i in my_string)

print(solution_2(a,3))
