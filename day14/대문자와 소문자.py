# 대문자와 소문자
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자
# 로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.


def swap_case(text):
    swapped_text = ""
    for char in text:
        if char.islower():
            swapped_text += char.upper()
        elif char.isupper():
            swapped_text += char.lower()
        else:
            swapped_text += char
    return swapped_text


print(swap_case("cccCCC"))
