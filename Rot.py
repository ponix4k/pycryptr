#!/usr/bin/python3
Alpha_Low = ('abcdefghijklmnopqrstuvwxyz')
Alpha_Up  = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


newMessage = ''
message = input('Please enter a message to encode: ')
Rot = input('Please Enter Rotation: ')
try:
 RotVal = int(Rot)
 print('Shift vaulue is: ',RotVal)
except ValueError:
 print('This is not an number please try again')
 Rot = input('Please Enter Rotation: ')

for Char in message:
 if Char in Alpha_Low:
  position = Alpha_Low.find(Char)
  newPosition = (position + RotVal) % 26
  newChar = Alpha_Low[newPosition]
  #print('The New character is is: ',newChar)
  newMessage += newChar
 elif Char in Alpha_Up:
  position = Alpha_Up.find(Char)
  newPosition = (position + RotVal) % 26
  newChar = Alpha_Up[newPosition]
  #print('The New character is is: ',newChar)
  newMessage += newChar
 else:
  newMessage += Char
print('Encrypted message is: ',newMessage)
