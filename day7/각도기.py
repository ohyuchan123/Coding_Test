# 각도기

# 문제 설명
#각에서 0도 초과 90도 미만은 예각,
# 90도는 직각, 90도 초과 
#180도 미만은 둔각 180도는 평각으로 분류합니다. 

#각 angle이 매개변수로 주어질 때 예각일 때 1,
# 직각일 때 2, 둔각일 때 3, 평각일 때 4를
# return하도록 solution 함수를 완성해주세요.

# 예각 : 0 < angle < 90
# 직각 : angle = 90
# 둔각 : 90 < angle < 180
# 평각 : angle = 180

# 제한 사항
# 0<angle<=180
# angle은 정수 입니다.

# 입출력 예
# angle : 70
# result : 1

# 입출력 예 설명
# angle이 70이므로 예각입니다. 따라서 1을 return입니다.

# 구현
angle = 70

if 0<angle<90:
    print(1)
elif angle==90:
    print(2)
elif 90<angle<180:
    print(3)
elif angle==180:
    print(4)


# 정답
def solution(angle):
    if 0<angle<90:
        return 1
    elif angle==90:
        return 2
    elif 90<angle<180:
        return 3
    elif angle==180:
        return 4
    
# 조금 더 분발하자
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer