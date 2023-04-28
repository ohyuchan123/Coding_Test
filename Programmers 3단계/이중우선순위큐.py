# 이중 우선 순위 큐

# 문제 설명
# 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

# 명령어    수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	    큐에서 최댓값을 삭제합니다.
# D -1	    큐에서 최솟값을 삭제합니다.

#이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
#모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 
#[최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

current = []
num = []
operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

for i in operations:
    current = i.split(' ')
    if current[0]=='I':
        num.append(int(current[1]))
    elif current[0]=='D':
        if current[1] == '-1':
            num.remove(min(num))
        elif current[1] == '1':
            num.remove(max(num))

print(num)