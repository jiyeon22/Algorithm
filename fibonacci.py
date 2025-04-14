i = 0
fibonacci_first = 0  #previous
fibonacci_second = 1 #current
fibonacci = 1        #임시 보관소 temp 이용하기

while i < 50:
    print(fibonacci)
    fibonacci = fibonacci_first + fibonacci_second
    fibonacci_first = fibonacci_second
    fibonacci_second = fibonacci
    i += 1


