N = int(input())

str_list = [] 
vowels = ['a','e','i','o','u']

for i in range(N):
	s = input()
	str_list.append(s)
	
for word in str_list:
	only_vowels = [ch for ch in word if ch.lower() in vowels]
	if only_vowels:
		print(''.join(only_vowels))
	else:
		print("???")