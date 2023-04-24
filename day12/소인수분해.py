# 소인수분해

# 문세 설명
# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.
# 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 
#따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 
#n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            d += 1
    return list(dict.fromkeys(answer))

print(solution(12))