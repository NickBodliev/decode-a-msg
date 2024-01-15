def extract_data(message_file):
	# Initialize an empty dictionary to store extracted data
	data = {}

	# Open the file in read mode
	with open(message_file, 'r') as file:
		# Iterate over each line in the file
		for line in file.readlines():
			# Split each line into words
			words = line.split()

			# Extract the first and second words (assuming the first is an integer and the second is a string)
			number = int(words[0])
			string_data = words[1]

			# Populate the dictionary
			data[number] = string_data

	# Return the populated dictionary
	return data

def create_sequence(highest_value):
	# Initialize an empty list to store the sequence
	sequence = []

	# Initialize variables for sequence generation
	decode_index = 1
	increment = 2

	# Generate the sequence based on the specified criteria
	while decode_index < highest_value:
		sequence.append(decode_index)
		decode_index += increment
		increment += 1

	# Return the generated sequence
	return sequence

def words_from_sequence(dict, sequence):

	# Initialize an empty list to store words from the dictionary based on the sequence
	words = []

	# Retrieve words from the dictionary based on the sequence
	for num in sequence:
		words.append(dict[num])

	# Return the list of words
	return words

def decode(message_file):
	# Extract data from the message file and create a dictionary
	dict = extract_data(message_file)

	# Find the highest key in the dictionary
	highest_key = int(max(dict.keys()))

	# Create a sequence of numbers based on the highest key
	sequence = create_sequence(highest_key)

	# Retrieve words from the dictionary based on the sequence
	words = words_from_sequence(dict, sequence)
	
	# Join the words into a sentence
	sentence = ' '.join(words)
	return sentence

# Example usage:
file_path = 'coding_qual_input.txt'
decoded_message = decode(file_path)
print(decoded_message)