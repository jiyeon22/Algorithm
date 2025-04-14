#list
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

#indexing
print(names[1])
print(numbers[1]+numbers[3])

#list slicing
numbers[0:4] #0부터 3까지
print(numbers[0:])
print(numbers[:2])

new_list = numbers[:3]
print(new_list)

print(len(numbers)) #길이 출력

numbers.append(5) #새로운 값을 list의 가장 오른쪽에 추가
print(numbers)

del numbers[3] #해당 인덱스값 삭제

print(numbers)

numbers.insert(4, 37) #4번 index에 37값 추가
print(numbers)


new_list = sorted(numbers) #sorted정렬 : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
print(new_list)
new_list = sorted(numbers, reverse=True)  #거꾸로 정렬
print(new_list)

numbers.sort() #sort정렬 : 아무것도 리턴하지 않고, 기존 리스트를 정렬
print(numbers)

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1) #라운드함수 >반올림 (소수점1째자리)
    i += 1
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력
