f = open("encrypt.txt", "r+")
l = open("decrypt.txt", "r+")


cipherText = f.read()
# This opens the text file with the encrypted code in it
asciiCodes = []
asciiValues = [] 
message = []
# This defines the lists that I will use in the program. They are all empty for now but 
# values will be added later on.
looper = 0
shiftNumber = 1

while shiftNumber < 96:
	# This changes every single character in the code to its corresponding ASCII number
	for letter in cipherText:
		number = ord(letter)
		asciiCodes.append(number)
	
	# This will add what ever shiftNumber the program is at to the numbers from the previous
	# loop and turn it into its corresponding ASCII character 
	for value in asciiCodes:
		if value + shiftNumber > 126:
			# If any value is over 126, it changes it to its corresponding value by subtracting 95 from it
			asciiValues.append(value + shiftNumber - 95)
		else:
			asciiValues.append(value + shiftNumber)
		
	
	#This will change the numbers in the list to their corresponding ASCII characters 
	#It also appends all of the new characters to a new list called "message"
	for character in asciiValues:
		alphabet = chr(character)
		message.append(alphabet)

	#This will add every single character back to the file 
	for character in message:
		l.write(character)
		
	l.write("\n")
	# This code will change the number of letters shifted every time the program runs 
	shiftNumber += 1
	# This resets the previous lists so they can be used again.
	asciiCodes = []
	asciiValues = []
	message = [] 

	
print("Everything has been decoded, check the file.")
f.close()
l.close()
	