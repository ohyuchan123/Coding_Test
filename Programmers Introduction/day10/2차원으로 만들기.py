# 2차원으로 만들기

# 문제 설명

# 정수 배열 num_list와 정수 n이 매개변수로 주어집니다.
# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return 하도록
# solution 함수를 완성해주제요

num_list = [1,2,3,4,5,6,7,8]
n = 2

def solution(num_list,n):
    return [num_list[i-n:i] for i in range(n,len(num_list)+1,n)]

print(solution(num_list,n))