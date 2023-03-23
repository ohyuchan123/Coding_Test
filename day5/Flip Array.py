#정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

num = [1,2,3,4,5]
num= num[::-1]
print(num)

def solution(num_list):
    return num_list[::-1]