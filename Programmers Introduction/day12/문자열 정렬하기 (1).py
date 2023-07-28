# 문자열 정렬하기(1)

# 문제 설명
#문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라
# 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

import re

def solution(my_string):
    return  sorted(list(map(int,re.sub(r'[^0-9]', '', my_string))))

print(solution("hi12392"))

# r'[^0-9]'는 정규표현식(regular expression) 패턴 중 하나로, 숫자를 제외한 모든 문자를 찾을 때 사용합니다.

# 예를 들어, re.findall(r'[^0-9]', 'abc123def456')를 실행하면 'a', 'b', 'c', 'd', 'e', 'f'와 같은 결과가 반환됩니다.
#  이는 문자열 'abc123def456'에서 숫자를 제외한 모든 문자를 찾아낸 것입니다.


# list_a = ['1', '2', '3', '4']   -> list_a = [1, 2, 3, 4] 로 바꾸고 싶을 때,

# python 3. list_a = list(map(int, list_a))
