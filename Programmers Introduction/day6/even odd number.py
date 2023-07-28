# 짝수 홀수 개수
#정수가 담긴 리스트 num_list가 주어질 때, 
#num_list의 원소 중 짝수와 홀수의 개수를 담은 
#배열을 return 하도록 solution 함수를 완성해보세요.

a = [1,2,3,4,5]
b = [1, 3, 5, 7]
result=[]

even = odd = 0
for num in a:
    if num%2==0:
        even +=1
    else:
        odd+=1

print(even,odd)


# 함수로 구현
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

print(solution(a))
