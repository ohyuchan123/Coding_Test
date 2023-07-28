# 특정 문자 제거하기

# 문제 설명
# 문자열 `my_string`과 문자 `letter`이 매개변수로 주어집니다.
# `my_string`에서 `letter`를 제거한 문자열을 return하도록 solution 함수를 완성해주세요

# 제한 사항
# 1 <= `my_string`의 길이 <=100
# `letter`은 길이가 1인 영문자 입니다.
# `my_string`과 `letter`은 알파벳 대소문자로 이루어져 있습니다.
# 대문자와 소문자를 구분합니다.

# 입출력 예
# my_string : "absdef"
# letter : "f"
# result : "abcde"

# 입출력 예 설명
# "abcdef"에서 "f"를 제거한 "abcde"를 return 합니다.

# 구현

my_string = 'abcdef'
search = 'f'


print(my_string.replace(search,' '))

# 정답

def solution(my_string, letter):
    return my_string.replace(letter,'')