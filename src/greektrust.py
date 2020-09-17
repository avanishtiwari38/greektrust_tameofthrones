import sys
from collections import Counter
from constant import *

def caesar_encrypt(realText, step):
	outText = ''
	for eachLetter in realText:
		if eachLetter in UPPERCASE:
			index = UPPERCASE.index(eachLetter)
			crypting = (index + step) % 26
			newLetter = UPPERCASE[crypting]
			outText = outText + newLetter
	return outText


def format_input(kingdom, message):
    message_dict = {}
    message_dict[kingdom] = Counter(message.replace(" ","").replace('"',""))
    flag = True
    key = len(DATA_KINGDOM[kingdom])
    look_up_dict = {}
    look_up_dict[kingdom] = Counter(caesar_encrypt(DATA_KINGDOM[kingdom], len(DATA_KINGDOM[kingdom])))
    for ch in look_up_dict[kingdom]:
    	if look_up_dict[kingdom][ch] > message_dict[kingdom][ch] and look_up_dict[kingdom][ch] != message_dict[kingdom][ch]:
    		flag = False

    return flag

def check_msg(data):
	total_frnd = ['SPACE']
	if len(data) < 3:
		return None

	for kingdom in data:
		if kingdom in DATA_KINGDOM:
			found_king = format_input(kingdom, data[kingdom])
			if found_king:
				total_frnd.append(kingdom)

	if len(total_frnd) >= 4:
		return total_frnd
	else:
		return None


def readInput():
	try:
		readData = {}
		if len(sys.argv) < 2:
			return "Input file .txt is required Please enter the path for your file"

		with open(sys.argv[1], 'r') as f:
		    lines = f.readlines()
		    for line in lines:
		    	if line.strip():
		    		kingdom_text = line.strip().split(" ",1)
		    		readData[kingdom_text[0]] = kingdom_text[1]

		data = check_msg(readData)
		return " ".join(data)

	except FileNotFoundError as e:
		return "No such file or directory: 'xyz.txt'"
	except Exception as e:
		# return str(e)
		raise e


if __name__ == '__main__':
	output = readInput()
	print(output)


