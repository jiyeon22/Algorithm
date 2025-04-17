n = int(input())  # 과제 수
tasks = []

for _ in range(n):
    line = input()  # ex: 5/1 7/1
    start_str, end_str = line.strip().split()
    sm, sd = map(int, start_str.split('/'))
    em, ed = map(int, end_str.split('/'))

    start = sm * 100 + sd  # 날짜를 정수로 표현
    end = em * 100 + ed
    tasks.append((start, end))

# 시작일 오름차순, 같으면 종료일 내림차순
tasks.sort(key=lambda x: (x[0], -x[1]))

events = []
for i in range(n):
    events.append((tasks[i][0], i + 1))   # 시작: 양수
    events.append((tasks[i][1], -i - 1))  # 종료: 음수

# 시간 기준 정렬
events.sort()

stack = []
for time, idx in events:
    if idx > 0:
        stack.append(idx)  # 시작 구간 push
    else:
        if stack and stack[-1] == -idx: #스택이 비어있지 않고, 가장 최근에 시작한 과제의 번호가 -idx이면 실행.
            stack.pop()  # 정상적인 짝 → pop
        else:
            print("No")
            exit()  # 짝이 안 맞으면 즉시 종료

print("Yes")
