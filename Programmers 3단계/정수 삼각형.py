# 정수 삼각형

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)): # 7
        for j in range(len(triangle[i])):
            if j == 0:
               triangle[i][j]+=triangle[i-1][j] # 3 +=7 10
            elif j == len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1] #
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    answer = max(triangle[-1])
    return answer

for i in range(1,len(triangle)):
    print(len(triangle[i]))