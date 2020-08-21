q = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
score = 0

import random
print("歡迎來到英文高高手英打測驗")
while True:
    op=int(input("開始請按1開始，按0結束"))
    if op==0:
        break
    while True:
        times =int(input("單字數量20~90"))
        if times <= 90 and times >= 20:
            break
        else:
            print('輸入超過範圍')
    if op == 1:
        for i in range(times):
            a= int(random.randint(0,25))
            b=q[a]
            ans =input(b)
            if ans == b:
                print("答對")
                score += 1
            else:
                print("答錯扣一分")
                score -=1
    break
if op != 0:
    print(score)
print("感謝使用")
ans = input("要玩小遊戲嗎?(要玩輸入1不要輸入2)")
if ans==1:
    ans = input('地雷1 蛇2 2048:3')
    if ans == 1
            
