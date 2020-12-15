def compare_string(label_list, stt_list) :
	color_len = len(stt_list) if len(stt_list) > len(label_list) else len(label_list)
	color_list = [['0' for _ in range(3)] for _ in range(color_len)]
	num1 = 0
	num2 = 0
	color = ''

	for i in stt_list :
		for j in i :
			if j in label_list[num1][num2] :
				if j != '-' :
					color_list[num1][num2] = '1'
			num2 = num2 + 1
		num1 = num1 + 1

		if (num1 >= len(label_list)) :
			for i in range(len(label_list), len(stt_list)) :
				for j in range(0,3) :
					color_list[i][j] = '0'
			break

		num2 = 0

	stt_list = sum(stt_list, [])
	stt_list = "".join(stt_list)

	color_list = sum(color_list, [])

	accuracy_num = 0

	for i in color_list :
		if i=='1' :
			accuracy_num = accuracy_num + 1;
		color = color + i

	accuracy = int((accuracy_num / len(color_list)) * 100)

	print(stt_list)
	print(color)
	print(accuracy)
