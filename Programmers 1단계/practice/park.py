# 공원 산책

# 문제 설명 부분은 프로그래머스 내에서 확인하기
# 1단계 공원 산책 문제


# park
# -> S : 시작 지점 O : 이동 가능한 통로 X : 장애물

#routes
# -> N : 북쪽으로 주어진 칸만큼 이동합니다.
# -> S : 남쪽으로 주어진 칸만큼 이동합니다.
# -> W : 서쪽으로 주어진 칸만큼 이동합니다.
# -> E : 동쪽으로 주어진 칸만큼 이동합니다.

#입출력 예
# ["SOO","OOO","OOO"] : park
# ["E 2","S 2","W 1"] : routes
# [2,1] : result


#입력된 명령대로 동쪽으로 2칸,
# 남쪽으로 2칸, 서쪽으로 1칸 
#이동하면 [0,0] -> [0,2] -> [2,2] -> [2,1]이 됩니다.

# 첫 번째 구현 : S,O,X를 구분 및 개수 출력 - 03/27 목표
from collections import Counter
a = ["SOO","OOO","OOO"]

# Counter를 사용하기 위해서는 문자열을 합쳐야 하기 때문에 join함수를 사용할 것이다.
result = ''.join(a)
print(result)

# 이제 Counter 함수를 이용하여 개수를 출력해보자
print(Counter(result))

# 위 조건은 조건으로는 S가 정확하게 어디에 있고 몇번째에서 시작하는지 알 수 없어서
# 다른 조건으로 만들어 보았다.

# 조건 : S 어디에 있는지 인덱스 번호 - 03/30
park = ["SOO","OOO","OOO"]
park_2 = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 2","W 1"]


answer = []
start = []

for i in range(len(park)):
        if 'S' in park[i]:
            start = [i, park[i].find('S')]
            break


print(start)

# 조건  : routes 분리 - 03/30
for route in routes:
        dir, move = route.split(' ')
        move = int(move)
        print(dir)
        print(move)


# 코드 조건 구현 -> 03/31
def solution(park, routes):
    answer = []
    start = []

    for i in range(len(park)):
        if 'S' in park[i]:
            start = [i, park[i].find('S')]
            break

    for route in routes:
        dir, move = route.split(' ')
        move = int(move)

        if dir == 'E':
            loc = start[1] + move
            if loc >= len(park[0]):
                continue
            if 'X' in park[start[0]][start[1]+1:loc+1]:
                continue
            else:
                start[1] = loc

        elif dir == 'W':
            loc = start[1] - move
            if loc < 0:
                continue
            if 'X' in park[start[0]][loc:start[1]]:
                continue
            else:
                start[1] = loc

        elif dir == 'S':
            loc = start[0] + move
            if loc >= len(park):
                continue
            if 'X' in [park[i][start[1]] for i in range(start[0]+1,loc+1)]:
                continue
            else:
                start[0] = loc

        elif dir == 'N':
            loc = start[0] - move
            if loc < 0:
                continue
            if 'X' in [park[i][start[1]] for i in range(loc,start[0])]:
                continue
            else:
                start[0] = loc

    return start