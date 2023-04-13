# 외계행성의 나이

#문제 설명
#우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. 
#a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
#나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

# 아스키 코드 사용하기
def solution(age):
    answer = ''
    return answer.join([chr(int(i)+97) for i in str(age)])
    # 위 코드는 age를 가져와 문자열로 변환한 다음 각 문자를 반복합니다. 각 문자에 대해 문자를 정수로 변환하고 97을 더합니다.

    # 예) 23이 숫자로 들어왔을 때 문자열로 변환 '23' i값에 분리해서 저장
    # 2,3 이를 아스키 코드값에 작성

print(solution(23))

age = 23