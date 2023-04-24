# 삼각형의 완성조건 (1)

# 문제 설명
# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

#가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
#삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

a = [1,2,3]

def solution(sides):
    sort_list = sorted(sides)
    if sort_list[0]+sort_list[1]>sort_list[2]:
        return 1
    else:
        return 2

print(solution(a))
