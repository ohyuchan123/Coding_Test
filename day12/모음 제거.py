# 모음 제거

# 문제 설명
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

a = ['a','e','i','o','u']
my_string = "bus"

list = list(my_string)

for i,element in enumerate(my_string):
    for j in range(len(a)):
        if element == a[j]:
            list.remove(a[j])
result = ''.join(list)
print(result)

