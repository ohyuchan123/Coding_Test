#최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
#정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
# 최빈값이 여러 개면 -1을 return 합니다.

#a = [1, 2, 3, 3, 3, 4]
a=[1, 1, 2, 2]
#a=[1]

# for i in enumerate(a):
#     print(i)

# for i,b in enumerate(set(a)):
#     a.remove(b)

# print(a)

def solution(array):
    if len(array) < 2:
        return array[0]
    
    while len(array)!=0:
        for i, b in enumerate(set(array)):
            array.remove(b)
        if i==0:
            return array[0]
    return -1

print(solution(a)) #-> 프로그래머스 채점 기준에 안 맞음 (테스트 모두 성공)


from collections import Counter
def solution(array):
    c = Counter(array).most_common()
    print(c)
    if len(c) > 1 and c[0][1] == c[1][1]:
        return -1
    
    return c[0][0]