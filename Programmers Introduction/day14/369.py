# 369 게임

# 문제 설명
#머쓱이는 친구들과 369게임을 하고 있습니다. 
#369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 
#3, 6, 9의 개수만큼 박수를 치는 게임입니다. 머쓱이가 말해야하는 숫자 order가 
#매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

order = 29423	
order_list = list(map(int,str(order)))

print(type(order_list))

cnt = 0

for i in range(len(order_list)):
    if order_list[i]==3 or order_list[i] == 6 or order_list[i]==9:
        cnt+=1
print(cnt)
        

