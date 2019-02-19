#!/usr/bin/python3

#This is a simple Rotatonal Encoder/Decoder that will shift letters around based on the value given

#CharTypes
Alpha_Low = ('abcdefghijklmnopqrstuvwxyz') #set up array of lowercase characters
Alpha_Up  = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #set up array of uppercase characters

#Message
newMessage = ''
message = input('Please enter a message to encode/decode: ') #request message from user
Rot = input('Please Enter Rotation (0 for all) : ') #request rotation amount e.g rot 2 a = c

#Lowercase Search
for Char in message:
 if Char in Alpha_Low:
  position = Alpha_Low.find(Char)
  newPosition = (position + RotVal) % 26
  newChar = Alpha_Low[newPosition]
  newMessage += newChar

#Uppercase Search
 elif Char in Alpha_Up:
  position = Alpha_Up.find(Char)
  newPosition = (position + RotVal) % 26
  newChar = Alpha_Up[newPosition]
  newMessage += newChar

 else:
  newMessage += Char
print('Encoded/Decoded message is: ',newMessage)
