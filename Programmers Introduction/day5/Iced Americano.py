#머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
#아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 
#가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 
#최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 
#담은 배열을 return 하도록 solution 함수를 완성해보세요.머쓱이는 
#추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 
#머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 
#아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

#간단하게 구현
import math
money = 5500
answer = []

answer.insert(0,math.ceil(money/5500))
answer.insert(1,money%5500)
print(answer)

def solution(money):
    ice = 5500
    answer=[]
    
    if money%ice==0:
        answer.insert(0,math.ceil(money/5500))
        answer.insert(1,money%5500)
    else:
        answer.insert(0,math.ceil(money/5500)-1)
        answer.insert(1,money%5500)
    return answer

print(solution(15000))