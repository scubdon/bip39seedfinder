# Finds BIP39 seed phrases in a text file ('filetosearch.txt') and prints them to the console

# open the file to search through, read the text, and split it into a list of words
with open('filetosearch.txt', 'r') as f:
  text = f.read()

words = text.split()

# Split the bip39 seed words file into a list of strings, and create a dictionary of those strings
with open('bip39seedwords.txt', 'r') as f:
  strings = f.read()

strings_list = strings.split()

strings_dict = {string: True for string in strings_list}

for i in range(len(words)):
  count = 0
  cur_sequence = []
  for j in range(i, len(words)):
    if words[j] in strings_dict:
      cur_sequence.append(words[j])
      count += 1
    else:
      break
  if count >= 12:
    print(cur_sequence)