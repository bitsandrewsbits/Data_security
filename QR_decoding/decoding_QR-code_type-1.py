# decoding QR-code version-1

example_of_QR_code = [[1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
					  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
  					  [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1], 
  					  [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1], 
					  [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1], 
					  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
					  [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
					  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
					  [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], 
					  [0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1], 
					  [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1], 
					  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
					  [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], 
					  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0], 
					  [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
					  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0], 
					  [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
					  [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], 
					  [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1], 
					  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], 
					  [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]
]

mask = 0

def decode_QR_code_version_1():
	# for right vertical code design
	pass


def get_content_part_from_QR_code(QR_as_2D_array = [[1, 1], [0, 1]]):
	rows_amount = 8
	columns_amount = 12

	start_content_column = 13
	start_content_row = 9

	result_QR_code_content_part = []
	current_writing_row = -1
	for i in range(len(QR_as_2D_array)):
		if i >= start_content_row:
			result_QR_code_content_part.append([])
			current_writing_row += 1
		for j in range(len(QR_as_2D_array[i])):
			if i >= 11 and (j == 13 or j == 14):
				result_QR_code_content_part[current_writing_row].append('n')
			elif i >= start_content_row and j >= start_content_column:
				result_QR_code_content_part[current_writing_row].append(QR_as_2D_array[i][j])

	return result_QR_code_content_part

def show_matrix_in_pretty_format(arr_2d = [[0, 0],[1, 1]]):
	for i in range(len(arr_2d)):
		print(arr_2d[i])


def reading_data_from_QR_content_part(QR_content_part = [[1, 0], [0, 1]]):
	result_bits_string = ''

	rows_index_i = len(QR_content_part) - 1
	columns_index_j = len(QR_content_part[0]) - 1
	movement_vector_for_read_QR_content = 'up'
	QR_content_bit_amount = len(QR_content_part) * len(QR_content_part[0])
	QR_row_max_index = len(QR_content_part) - 1
	for _ in range(0, QR_content_bit_amount):
		if len(result_bits_string) == QR_content_part:
			break

		print(f'Current- coordinats: ({rows_index_i}, {columns_index_j})')
		result_bits_string += str(QR_content_part[rows_index_i][columns_index_j])

		# first phase - from down to up	
		if rows_index_i > 0 and columns_index_j % 2 != 0 and movement_vector_for_read_QR_content == 'up':
			columns_index_j -= 1
		elif rows_index_i > 0 and columns_index_j % 2 == 0 and movement_vector_for_read_QR_content == 'up':
			columns_index_j += 1
			rows_index_i -= 1

		# link between first and second algorithm phases
		if rows_index_i == 0 and len(QR_content_part[:columns_index_j + 1]) % 4 == 0:
			upper_arr_from_left_to_right = QR_content_part[rows_index_i][-2:][::-1]
			upper_str_arr_from_left_to_right = [str(bit) for bit in upper_arr_from_left_to_right]
			result_bits_string += ''.join(upper_str_arr_from_left_to_right)
			columns_index_j -= 2
			movement_vector_for_read_QR_content = 'down'
			print(upper_str_arr_from_left_to_right)
			print('Changing vector of reading to BOTTOM!')
			continue
		
		# second phase - from up to down
		if rows_index_i < QR_row_max_index and columns_index_j % 2 != 0 and movement_vector_for_read_QR_content == 'down':
			columns_index_j -= 1
		elif rows_index_i < QR_row_max_index and columns_index_j % 2 == 0 and movement_vector_for_read_QR_content == 'down':
			columns_index_j += 1
			rows_index_i += 1
		
		# link from second -> first phase of algorithm
		if rows_index_i == QR_row_max_index and movement_vector_for_read_QR_content == 'down':
			bottom_arr_from_right_to_left = QR_content_part[rows_index_i][columns_index_j - 1:columns_index_j + 1][::-1]
			bottom_str_arr_from_right_to_left = [str(bit) for bit in bottom_arr_from_right_to_left]
			result_bits_string += ''.join(bottom_str_arr_from_right_to_left)
			columns_index_j -= 2
			movement_vector_for_read_QR_content = 'up'
			print(bottom_str_arr_from_right_to_left)
			print('Changing vector of reading to UP!')

	return result_bits_string

content_part_of_QR_code = get_content_part_from_QR_code(example_of_QR_code)
show_matrix_in_pretty_format(content_part_of_QR_code)

res_bits_string = reading_data_from_QR_content_part(content_part_of_QR_code)
print(res_bits_string)
print('bits length =', len(res_bits_string))

