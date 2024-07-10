import random

def String_has_five_diff_char(string):
	count = 0
	array = []
	for i in string:
		if i not in array:
			array.append(i)
			count += 1
		if count >= 5:
			return True
	return False

def find_loop(string):
	array = [0] * 256
	for char in string:
		array[ord(char)] += 1
	character_max = []
	character_min = []
	counter = [0, len(string) + 1]
	for i in range(256):
		if array[i] > counter[0]:
			counter[0] = array[i]
			character_max = [chr(i)]
		elif array[i] == counter[0]:
			character_max.append(chr(i))
		if array[i] > 0 and array[i] < counter[1]:
			counter[1] = array[i]
			character_min = [chr(i)]
		elif array[i] == counter[1]:
			character_min.append(chr(i))
	return random.choice(character_max), counter[0], random.choice(character_min), counter[1]

array = []
index = 2

while len(array) < index:
	string_index = input(f"Nhập chuỗi {len(array) + 1}: ")
	if not String_has_five_diff_char(string_index):
		print("Chuỗi này chưa có 5 ký tự khác nhau. Vui lòng nhập lại.")
	else:
		array.append(string_index)

for i, string in enumerate(array):
	print(f"Chuỗi {i + 1}: {string}")
	print(f"Ký tự lập lại nhiều nhất là {find_loop(string)[0]} với số lần lập là {find_loop(string)[1]}")
	print(f"Ký tự lập lại ít nhất là {find_loop(string)[2]} với số lần lập là {find_loop(string)[3]}")