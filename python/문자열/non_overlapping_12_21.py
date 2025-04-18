s = input()

pos_21 = s.find("21")
pos_12 = s.find("12")

#21 먼저 찾고 그 다음에 12나오는 경우
#문자열 안에 21이 있는 경우 실행하겠다. -1이라면 해당 문자열 안에 없는 것. 
if pos_21 != -1:
    next_12 = s.find("12", pos_21 + 2)
    if next_12 != -1:
        print("Yes")
        exit() #프로그램 전체 종료  

if pos_12 != -1:
    next_21 = s.find("21", pos_12 + 2)
    if next_21 != -1:
        print("Yes")
        exit() 

print("No") #12,21이 겹치는 경우 또는 없는 경우