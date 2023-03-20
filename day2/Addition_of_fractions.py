#첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
#두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
#두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을
#return 하도록 solution 함수를 완성해보세요.

# 코드를 간편화 하기 위해서는 최대공약수를 사용해야 되고 그러기 위해서는 math import를 불러와야 한다
import math

def solution(numer1, denom1, numer2, denom2):
    answer=[0,1]
    number = denom1*numer2+denom2*numer1 #분자
    denom = denom1 * denom2 # 분모

    gcd = math.gcd(denom,number) #최대공약수

    answer[0] = number//gcd 
    answer[1] = denom//gcd

    return answer
    

print(solution(1,2,3,4))