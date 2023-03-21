#정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 
#담긴 배열을 return하도록 solution 함수를 완성해주세요.
a=15
result=[]
for i in range(a+1):
    if i%2!=0:        
        result.append(i)

print(result)



# 함수로 제작
def solution(a):
    result=[]
    for i in range(a+1):
        if i%2!=0:        
            result.append(i)

    return result
        