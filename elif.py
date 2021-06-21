'''def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")
    # 코드를 쓰세요.


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)


#제어문 100이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 값 출력
num = 0
while num <= 100:
    if (num%12) != 0:
        print(num)
    num += 8


#1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력
num=1
sum=0

while num < 1000:
    if num % 2 == 0 or num % 3 == 0:
        sum +=num
        num +=1
    else:
        num +=1

print(sum)

#else빼고 if문 밖에 num +=1 해도됨

#약수 찾기
i=1
n=120
number=0

while i <= n:
    if n % i == 0:
        print(i)
        number += 1
    i += 1
print("{}의 약수는 총 {}개입니다.".format(n, number))
'''
#택이의 우승 상금
year = 1989
prize_money = 50000000
apart_price = 1100000000 #상수 -> 대문자로 선언하자.

while year <= 2016:
    interest = prize_money * 0.12
    prize_money += interest
    year += 1

if prize_money > apart_price:
        print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(prize_money-apart_price)))
else:
        print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(apart_price-prize_money)))



