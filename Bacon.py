#!/usr/bin/python3

#This is a simple Bacon Encoder/Decoder that will Encode/Decode useing the bacon cipher

#Character Setup
Dict = {'A' : 'AAAAA','B' : 'AAAAB','C' : 'AAABA','D' : 'AAABB','E' : 'AABAA',
	'F' : 'AABAB','G' : 'AABBA','H' : 'AABBB','I' : 'ABAAA','J' : 'AVAAB',
	'K' : 'ABABA','L' : 'ABABB','M' : 'ABBAA','N' : 'ABBAB','O' : 'ABBBA',
	'P' : 'ABBBB','Q' : 'BAAAA','R' : 'BAAAB','S' : 'BAABA','T' : 'BAABB',
	'U' : 'BABAA','V' : 'BABAB','W' : 'BABBA','X' : 'BABBB','Y' : 'BBAAA',
	'Z' : 'BBAAB'}

#function To Encode into the bacon cipher
def encrypt(message):
	cipher = ''
	for letter in message:
		if(letter != ' '):  #Check message array for a space
			cipher += Dict[letter]  # find the letter in the dictionary
		else:
			cipher += ' ' # add a space
	return cipher

#Message
print('V.01a')
print('This Version currently only accepts All caps messages')
message = input('Please enter a message to encode: ') #request message from user

# Function to decrypt the string
# according to the cipher provided
def decrypt(message):
    decipher = ''
    i = 0

    # emulating a do-while loop
    while True :
        # condition to run decryption till
        # the last set of ciphertext
        if(i < len(message)-4):
            # extracting a set of ciphertext
            # from the message
            substr = message[i:i + 5]
            # checking for space as the first
            # character of the substring
            if(substr[0] != ' '):
                '''
                This statement gets us the key(plaintext) using the values(ciphertext)
                Just the reverse of what we were doing in encrypt function
                '''
                decipher += list(Dict.keys())[list(Dict.values()).index(substr)]
                i += 5 # to get the next set of ciphertext

            else:
                # adds space
                decipher += ' '
                i += 1 # index next to the space
        else:
            break # emulating a do-while loop

    return decipher

def main():

    result = encrypt(message.upper())
    print (result)

if __name__ == '__main__':
    main()