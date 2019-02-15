#!/usr/bin/python3
Alpha_Low = ('abcdefghijklmnopqrstuvwxyz')
Alpha_Up  = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

<<<<<<< HEAD

newMessage = ''
message = input('Please enter a message to encode: ')
=======
newMessage = ''
message = input('Please enter a message to encode/decode: ')
>>>>>>> 5d8f06118df839cf2036f0c61fcfb7c0243b8191
Rot = input('Please Enter Rotation: ')
try:
 RotVal = int(Rot)
 print('Shift vaulue is: ',RotVal)
except ValueError:
 print('This is not an number please try again')
 Rot = input('Please Enter Rotation: ')

<<<<<<< HEAD
=======
#Lowercase Search
>>>>>>> 5d8f06118df839cf2036f0c61fcfb7c0243b8191
for Char in message:
 if Char in Alpha_Low:
  position = Alpha_Low.find(Char)
  newPosition = (position + RotVal) % 26
  newChar = Alpha_Low[newPosition]
  #print('The New character is is: ',newChar)
  newMessage += newChar
<<<<<<< HEAD
=======
  
  #Uppercase Search
>>>>>>> 5d8f06118df839cf2036f0c61fcfb7c0243b8191
 elif Char in Alpha_Up:
  position = Alpha_Up.find(Char)
  newPosition = (position + RotVal) % 26
  newChar = Alpha_Up[newPosition]
  #print('The New character is is: ',newChar)
  newMessage += newChar
 else:
  newMessage += Char
<<<<<<< HEAD
print('Encrypted message is: ',newMessage)
=======
print('Encoded/Decoded message is: ',newMessage)
>>>>>>> 5d8f06118df839cf2036f0c61fcfb7c0243b8191
