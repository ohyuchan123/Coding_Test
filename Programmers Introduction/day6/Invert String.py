# Invert String(문자열 뒤집기)

#문제 설명
#문자열 my_string이 매개변수로 주어집니다.
# my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

# 리스트의 reverse를 이용해서 문자열 뒤집기
name1 = "jaron"
print(f'name1     : {name1}')

# 문자열을 리스트로
name_list = list(name1)  
print(f'name_list : {name_list}')

# 리스트 역순으로
name_list.reverse() 
print(f'name_list : {name_list}')

# 리스트를 문자열로
name2 = ''.join(name_list)
print(f'name2     : {name2}')

# 함수로 제작
def solution(my_string):
    string_list = list(my_string) # 문자열을 리스트로
    string_list.reverse() # reverse() 문자열을 뒤집어 주는 함수
    result = ''.join(string_list)
    return result

print(solution(name1))