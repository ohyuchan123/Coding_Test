# 공 던지기

# 문제 설명
# 머쓱이는 친구들과 동그랗게 서서 공 던지기 게임을 하고 있습니다.
# 공은 1번부터 던지며 오른쪽으로 한 명을 건너뛰고 그다음 사람에게만 던질 수
#있습니다.

#친구들의 번호가 들어있는 정수 배열 numbers와 정수 K가 주어질 때,
# k번째로 공을 던지는 사람의 번호는 무엇인지 return 하도록 solution 함수를 완성해보세요.

# 조건 1
# numbers = [1,2,3,4]
# k = 2

# 조건 2
# numbers = [1,2,3,4,5,6]
# k = 5

# 조건 3
numbers = [1,2,3]
k = 3

# 0 throw =3
# 

# k만큼 반복문이 돌아야 하고

def solution(k,numbers):
    for i in range(k):
        if i ==0 : throw = numbers[i+2]
        if throw < numbers[-1]:
            return throw
        else:
            if len(numbers)%2==0:
                throw = numbers[0]
            else:
                throw = numbers[1]


print(solution(k,numbers))

# 위 코드는 아애 틀린문제인데 답은 구해짐 신기함 ㄷㄷ

def solution_2(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)] # numbers[1] = 2

print(solution_2(numbers,k))