#!/usr/bin/python3
# Python program to implement Morse Code Translator
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
# Dictionary representing the morse code chart
DICT_Morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.',
              'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.',
              'O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-',
              'V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----',
              '2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
              '7':'--...','8':'---..','9':'----.','0':'-----',',':'--..--',
              '.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',')':'-.--.-'}
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += DICT_Morse[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 0 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                 # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(DICT_Morse.keys())[list(DICT_Morse
                .values()).index(citext)]
                citext = ''

    return decipher

# Hard-coded driver function to run the program
def main():
    enc = input('Please make your selection (0 = encode 1 = decode): ')
    encVar = int(enc)

    message = input('Please enter a message to Encode/Decode: ') #request message from user
    if encVar > 0:
        result = encrypt(message.upper())
        print (result)
    else:
        result = decrypt(message)
        print (result)

# Executes the main function
if __name__ == '__main__':
    main()
