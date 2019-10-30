#!/usr/bin/python3
import binascii

def encode_string(string, enc):
	if(enc):
		return str(bin(int.from_bytes(string.encode(), 'big')))[2:]
	else:
		string = int('0b' + string, 2)
		return string.to_bytes((string.bit_length()+7) // 8, 'big').decode()

def main():
	string = input("input string to be encoded/decoded: ")
	enc = int(input("do you want to encode this string to binary [0/1]: "))
	enc = (enc < 1)
	print (enc)
	print(encode_string(string, enc))

if __name__ == "__main__":
	main()
