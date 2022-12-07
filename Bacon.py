#!/usr/bin/python3

#This is a simple Bacon Encoder/Decoder that will Encode/Decode using the bacon cipher

#Character Setup
Dict24 = {
    'a' : 'aaaaa','b' : 'aaaab','c' : 'aaaba','d' : 'aaabb','e' : 'aabaa',
    'f' : 'aabab','g' : 'aabba','h' : 'aabbb','i' : 'abaaa','j' : 'abaaa','k' : 'abaab',
    'l' : 'ababa','m' : 'ababb','n' : 'abbaa','o' : 'abbab','p' : 'abbba','q' : 'abbbb',
    'r' : 'baaaa','s' : 'baaab','t' : 'baaba','u' : 'baabb','v' : 'baabb','w' : 'babaa',
    'x' : 'babab','y' : 'babba','z' : 'babbb','A' : 'AAAAA','B' : 'AAAAB','C' : 'AAABA',
    'D' : 'AAABB','E' : 'AABAA','F' : 'AABAB','G' : 'AABBA','H' : 'AABBB','I' : 'ABAAA',
    'J' : 'ABAAA','K' : 'ABAAB','L' : 'ABABA','M' : 'ABABB','N' : 'ABBAA','O' : 'ABBAB',
    'P' : 'ABBBA','Q' : 'ABBBB','R' : 'BAAAA','S' : 'BAAAB','T' : 'BAABA','U' : 'BAABB',
    'V' : 'BAABB','W' : 'BABAA','X' : 'BABAB','Y' : 'BABBA','Z' : 'BABBB',
    '1' : '1','2' : '2','3' : '3','4' : '4','5' : '5','6' : '6','7' : '7','8' : '8',
    '9' : '9','0' : '0', '-' : '-'
}

Dict26 = {
    'A' : 'AAAAA','B' : 'AAAAB','C' : 'AAABA','D' : 'AAABB','E' : 'AABAA',
	'F' : 'AABAB','G' : 'AABBA','H' : 'AABBB','I' : 'ABAAA','J' : 'ABAAB',
	'K' : 'ABABA','L' : 'ABABB','M' : 'ABBAA','N' : 'ABBAB','O' : 'ABBBA',
	'P' : 'ABBBB','Q' : 'BAAAA','R' : 'BAAAB','S' : 'BAABA','T' : 'BAABB',
	'U' : 'BABAA','V' : 'BABAB','W' : 'BABBA','X' : 'BABBB','Y' : 'BBAAA',
	'Z' : 'BBAAB','a' : 'AAAAA','b' : 'AAAAB','c' : 'AAABA','d' : 'AAABB',
	'e' : 'AABAA','f' : 'AABAB','g' : 'AABBA','h' : 'AABBB','i' : 'ABAAA',
	'j' : 'ABAAB','k' : 'ABABA','l' : 'ABABB','m' : 'ABBAA','n' : 'ABBAB',
	'o' : 'ABBBA','p' : 'ABBBB','q' : 'BAAAA','r' : 'BAAAB','s' : 'BAABA',
	't' : 'BAABB','u' : 'BABAA','v' : 'BABAB','w' : 'BABBA','x' : 'BABBB',
	'y' : 'BBAAA','z' : 'BBAAB','1' : '1','2' : '2','3' : '3','4' : '4',
	'5' : '5','6' : '6','7' : '7','8' : '8','9' : '9','0' : '0', '-' : '-'
	}

HTB = {
       'A' : 'AAAAA','B' : 'AAAAB','C' : 'AAANA','D' : 'AAANN','E' : 'AANAA',
       'F' : 'AANAN','G' : 'AANNA','H' : 'AANNN','I' : 'ANAAA','J' : 'ANAAA',
       'K' : 'ANAAN','L' : 'ANANA','M' : 'ANANN','N' : 'ANNAA','O' : 'ANNAN',
       'P' : 'ANNNA','Q' : 'ANNNN','R' : 'NAAAA','S' : 'NAAAN','T' : 'NAANA',
       'U' : 'NAANN','V' : 'NAANN','W' : 'NANAA','X' : 'NANAN','Y' : 'NANNA',
       'Z' : 'NANNN','1' : '1','2' : '2','3' : '3','4' : '4','5' : '5',
       '6' : '6','7' : '7','8' : '8','9' : '9','0' : '0', '-' : '-'
       }

DictBee = {
    'A' : 'BBBBB','B' : 'BBBBZ','C' : 'BBBZB','D' : 'BBBZZ','E' : 'BBZBB',
	'F' : 'BBZBZ','G' : 'BBZZB','H' : 'BBZZZ','I' : 'BZBBB','J' : 'BZBBB',
    'K' : 'BZBBZ','L' : 'BZBZB','M' : 'BZBZZ','N' : 'BZZBB','O' : 'BZZBZ',
	'P' : 'BZZZB','Q' : 'BZZZZ','R' : 'ZBBBB','S' : 'ZBBBZ','T' : 'ZBBZB',
	'U' : 'ZBBZZ','V' : 'ZBBZZ','W' : 'ZBZBB','X' : 'ZBZBZ','Y' : 'ZBZZB',
	'Z' : 'ZBZZZ','1' : '1','2' : '2','3' : '3','4' : '4','5' : '5',
	'6' : '6','7' : '7','8' : '8','9' : '9','0' : '0', '-' : '-'
 }

DictAlice = {
    'A' : 'HHHHH','B' : 'HHHHA','C' : 'HHHAH','D' : 'HHHAA','E' : 'HHAHH',
	'F' : 'HHAHA','G' : 'HHAAH','H' : 'HHAAA','I' : 'HAHHH','J' : 'HAHHH',
    'K' : 'HAHHA','L' : 'HAHAH','M' : 'HAHAA','N' : 'HAAHH','O' : 'HAAHA',
	'P' : 'HAAAH','Q' : 'HAAAA','R' : 'AHHHH','S' : 'AHHHA','T' : 'AHHAH',
	'U' : 'AHHAA','V' : 'AHHAA','W' : 'AHAHH','X' : 'AHAHA','Y' : 'AHAAH',
	'Z' : 'AHAAA','a' : 'HHHHH','b' : 'HHHHA','c' : 'HHHAH','d' : 'HHHAA',
    'e' : 'HHAHH','f' : 'HHAHA','g' : 'HHAAH','h' : 'HHAAA','i' : 'HAHHH',
    'j' : 'HAHHH','k' : 'HAHHA','l' : 'HAHAH','m' : 'HAHAA','n' : 'HAAHH',
    'o' : 'HAAHA','p' : 'HAAAH','q' : 'HAAAA','r' : 'AHHHH','s' : 'AHHHA',
    't' : 'AHHAH','u' : 'AHHAA','v' : 'AHHAA','w' : 'AHAHH','x' : 'AHAHA',
    'y' : 'AHAAH','z' : 'AHAAA','1' : '1','2' : '2','3' : '3','4' : '4',
    '5' : '5','6' : '6','7' : '7','8' : '8','9' : '9','0' : '0', '-' : '-'
 }


print('V1.70')
print('This Version will accept numbers and both uppercase and lowercase letters and has 24 and 26 character options and also a s3cret b33 cod3r')
charset =input('Select charset (0 = 24 chars , 1 = 26 chars , 2 = HTB, 3 = Alice): ')
charsetVar = int(charset)
print('Do you want to encode or decode a messages ?')
enc = input('Please make your selection (0 = encode 1 = decode): ')
encVar = int(enc)

#Message

message = input('Please enter a message to Encode/Decode: ') #request message from user

#function To Encode into the bacon cipher
def encrypt(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):  #Check message array for a space
            if charsetVar == 1:
                cipher += Dict26[letter]
            elif charsetVar == 2:
                cipher += HTB[letter]
            elif charsetVar == 4:
                cipher += DictBee[letter]
            elif charsetVar == 3:
                cipher += DictAlice[letter]
            else:
                cipher += Dict24[letter] #
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
                if charsetVar == 1:
                    decipher += list(Dict26.keys())[list(Dict26.values()).index(substr)]
                elif charsetVar == 2:
                    decipher += list(HTB.keys())[list(HTB.values()).index(substr)]
                elif charsetVar == 4:
                    decipher += list(DictBee.keys())[list(DictBee.values()).index(substr)]
                elif charsetVar == 3:
                    decipher += list(DictAlice.keys())[list(DictAlice.values()).index(substr)]
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
    if encVar > 0:
        result = decrypt(message.upper())
        print ('Decoded message is: ',result)
    else:
        result = encrypt(message.upper())
        print ('Encode message is: ',result)

if __name__ == '__main__':
    main()
