#!/usr/bin/python3

#This is a simple Bacon Encoder/Decoder that will Encode/Decode using the bacon cipher

#Character Setup
Dict24 = {'a' : 'aaaaa','b' : 'aaaab','c' : 'aaaba','d' : 'aaabb','e' : 'aabaa',
'f' : 'aabab','g' : 'aabba','h' : 'aabbb','i' : 'abaaa','j' : 'abaaa','k' : 'abaab',
'l' : 'ababa','m' : 'ababb','n' : 'abbaa','o' : 'abbab','p' : 'abbba','q' : 'abbbb',
'r' : 'baaaa','s' : 'baaab','t' : 'baaba','u' : 'baabb','v' : 'baabb','w' : 'babaa',
'x' : 'babab','y' : 'babba','z' : 'babbb','A' : 'AAAAA','B' : 'AAAAB','C' : 'AAABA',
'D' : 'AAABB','E' : 'AABAA','F' : 'AABAB','G' : 'AABBA','H' : 'AABBB','I' : 'ABAAA',
'J' : 'ABAAA','K' : 'ABAAB','L' : 'ABABA','M' : 'ABABB','N' : 'ABBAA','O' : 'ABBAB',
'P' : 'ABBBA','Q' : 'ABBBB','R' : 'BAAAA','S' : 'BAAAB','T' : 'BAABA','U' : 'BAABB',
'V' : 'BAABB','W' : 'BABAA','X' : 'BABAB','Y' : 'BABBA','Z' : 'BABBB',
'1' : '1','2' : '2','3' : '3','4' : '4','5' : '5','6' : '6','7' : '7','8' : '8',
'9' : '9','0' : '0'}

Dict26 = {'A' : 'AAAAA','B' : 'AAAAB','C' : 'AAABA','D' : 'AAABB','E' : 'AABAA',
	'F' : 'AABAB','G' : 'AABBA','H' : 'AABBB','I' : 'ABAAA','J' : 'AVAAB',
	'K' : 'ABABA','L' : 'ABABB','M' : 'ABBAA','N' : 'ABBAB','O' : 'ABBBA',
	'P' : 'ABBBB','Q' : 'BAAAA','R' : 'BAAAB','S' : 'BAABA','T' : 'BAABB',
	'U' : 'BABAA','V' : 'BABAB','W' : 'BABBA','X' : 'BABBB','Y' : 'BBAAA',
	'Z' : 'BBAAB','a' : 'AAAAA','b' : 'AAAAB','c' : 'AAABA','d' : 'AAABB',
	'e' : 'AABAA','f' : 'AABAB','g' : 'AABBA','h' : 'AABBB','i' : 'ABAAA',
	'j' : 'AVAAB','k' : 'ABABA','l' : 'ABABB','m' : 'ABBAA','n' : 'ABBAB',
	'o' : 'ABBBA','p' : 'ABBBB','q' : 'BAAAA','r' : 'BAAAB','s' : 'BAABA',
	't' : 'BAABB','u' : 'BABAA','v' : 'BABAB','w' : 'BABBA','x' : 'BABBB',
	'y' : 'BBAAA','z' : 'BBAAB','1' : '1','2' : '2','3' : '3','4' : '4',
	'5' : '5','6' : '6','7' : '7','8' : '8','9' : '9','0' : '0'
	}


print('V1.20')
print('This Version will accept numbers and both uppercase and lowercase letters and has 24 and 26 character options')
charset =input('Select charset (0 = 24char , 1 = 26char): ')
charsetVar = int(charset)
print('Do you want to encode or decode a messages ?')
enc = input('Please make your selection (0 = encode 1 = decode): ')
encvar = int(enc)

#Message

message = input('Please enter a message to Encode/Decode: ') #request message from user

#function To Encode into the bacon cipher
def encrypt(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):  #Check message array for a space
            if charsetVar > 0:
                 cipher += Dict26[letter]  # find the letter in the dictionary
            else:
                cipher += Dict24[letter]  # find the letter in the dictionary
        else:
            cipher += ' '
    return cipher


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
                if charsetVar > 0:
                    decipher += list(Dict26.keys())[list(Dict26.values()).index(substr)]
                else:
                    decipher += list(Dict24.keys())[list(Dict24.values()).index(substr)]
                i += 5 # to get the next set of ciphertext
            else:
                decipher += ' '
                i += 1 # index next to the space
        else:
            break # emulating a do-while loop

    return decipher

def main():
    if encvar > 0:
        result = decrypt(message.upper())
        print ('Decoded message is: ',result)
    else:
        result = encrypt(message.upper())
        print ('Encode message is: ',result)

if __name__ == '__main__':
    main()
