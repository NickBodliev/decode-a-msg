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

def decode(message_file):
	dict = extract_data(message_file)

	return dict[158]

file_path = 'coding_qual_input.txt'
decoded_message = decode(file_path)
print(decoded_message)