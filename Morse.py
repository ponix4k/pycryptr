#!/usr/bin/python3
DICT_Morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
              'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
              'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
              'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----',
              '2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
              '7':'--...','8':'---..','9':'----.','0':'-----',',':'--..--',
              '.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart

enc = input('Please make your selection (0 = encode 1 = decode): ')
encVar = int(enc)

message = input('Please enter a message to Encode/Decode: ')
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += DICT_Morse[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decrypt(message):

    message += ' '
    decipher = ''
    citext = ''
    for letter in message:

        if (letter != ' '):
            i = 0
            citext += letter
        else:
             i += 1
             if i == 2 :
                decipher += ' '
             else:
                decipher += list(DICT_Morse.keys())[list(DICT_Morse
                .values()).index(citext)]
                citext = ''

    return decipher

def main():
    if encVar > 0:
        result = decrypt(message.upper())
        print ('Encoded Message: ',result)
    else:
        result = encrypt(message.upper())
        print ('Decoded Message: ',result)
if __name__ == '__main__':
    main()
