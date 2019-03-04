from PIL import Image
import binascii
import optparse

def rgb2hex(r,g,b):
	return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def hex2rgb(hexcode):
	return tuple(map(ord, hexcode[1:].decode('hex')))

def str2bin(messgae):
	binary = bin(int(binascii.hexlify(message), 16))
	return binary[2:]

def bin2string(binary):
	message = binascii.unhexlify('%x'(int('0b' +binary, 2)))
	return message

def encode(hexcode, digit):
	if hexcode[-1] in ('0','1','2','3','4','5'):
		hexcode = hexcode[:-1]+digit
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0','1'):
		return hexcode[-1]
	else:
		return None

######hide#####
def hide(filename, message):
	img = Image.open(filename)
	binary = str2bin(message) + '1111111111111110'
	if img.mode in('RGBA'):
		img = Image.convert('RGBA')
		datas = img.getdata()

		newData=[]
		digit= 0
		temp = ''
		for item in datas:
			if (digit < len(binary)):
				newpix = encode(rgb2hex(item[0], item[1], item[2]),binary[digit])
				if newpix == None:
					newData.append(item)
				else:
					R,G,B = hex2rgb(newpix)
					newData.append((r,g,b,255))
					digit += 1
			else:
				newData.append(item)

			img.putData(newData)
			img.save(filename, "png")
			return "Completed"
		return "Incorrect image mode, couldnt hide"

######retrive######
def retr(filename):
	img = image.open(filename)
	binary = ''

	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()

		for items in datas:
			digit = decode(rgb2hex(item[0],item[1],item[2]))
			if digit == None:
				pass
			else:
				binary = binary + digit
				if (binary[-16]== '1111111111111110'):
					print ("Success")
				return bin2string(binary[:-16])
			return bin2string(binary)
			return "Incorrect image mode, couldnt retrive data"

def main():
	parser = optparse.OptionPaser('usage %prog'+\
		'-e/-d <targetfile>')
	parser.add_option(-e,dest='hide',type='string',\
		help='target picture to hide text')
	parser.add_option(-d, dest='retr',type='string',\
		help='target picture to retrive text')

	(options, args) = parser.parse_args()
	if (options.hide != None):
		text = raw_input("Enter a message to hide: ")
		print hide(options.hide, text)
	elif (options.retr != None):
		print retr(options.retr)
	else:
		print parser.usage
		exit(0)

if __Name__ == '_main__':
	Main()
