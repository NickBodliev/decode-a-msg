def extract_data(message_file):
	data = {}
	with open(message_file, 'r') as file:
		for line in file.readlines():
			# Split each line into words
			words = line.split()

			# Extract the first and second words (assuming the first is an integer and the second is a string)
			number = int(words[0])
			string_data = words[1]

			# Populate the dictionary
			data[number] = string_data
	return data

def create_sequence(highest_value):
	sequence = []
	decode_index = 1
	increment = 2
	while decode_index < highest_value:
		sequence.append(decode_index)
		decode_index += increment
		increment += 1
	return sequence

def words_from_sequence(dict, sequence):
	words = []
	for num in sequence:
		words.append(dict[num])
	return words

def decode(message_file):
	dict = extract_data(message_file)
	highest_key = int(max(dict.keys()))

	sequence = create_sequence(highest_key)
	words = words_from_sequence(dict, sequence)
	

	return words

file_path = 'coding_qual_input.txt'
decoded_message = decode(file_path)
print(decoded_message)