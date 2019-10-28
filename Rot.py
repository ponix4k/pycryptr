#!/usr/bin/python3

#This is a simple Rotatonal Encoder/Decoder that will shift letters around based on the value given

#CharTypes
alpha_low = ('abcdefghijklmnopqrstuvwxyz') #set up array of lowercase characters
alpha_up  = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #set up array of uppercase characters

def rotate(char, rot_val):
	if char in alpha_low:
		position = alpha_low.find(char)
		new_position = (position + rot_val) % 26
		new_char = alpha_low[new_position]
	elif char in alpha_up:
		position = alpha_up.find(char)
		new_position = (position + rot_val) % 26
		new_char = alpha_up[new_position]

	return new_char

def encode(message, rot_val):
	encoded_message = ''
	for char in message:
		encoded_message += rotate(char, rot_val)
	return encoded_message

def main():
	message = input('Please enter a message to encode/decode: ')
	rot = int(input('Please enter rotation factor: '))
	print("Encoded/Decoded message: {0}".format(encode(message, rot)))

if __name__ == "__main__":
	main()
