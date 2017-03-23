def alphabet_position(letter):
	alpha = "abcdefghijklmnopqrstuvwxyz"  
	lowercase = letter.lower()
	lposition = alpha.find(lowercase)
	return lposition


def rotate_character(char, rot):
	
	alpha = "abcdefghijklmnopqrstuvwxyz"
	ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	if char.isalpha():
		position = alphabet_position(char)
		if char in alpha:
			rotatelow = position + rot
			return alpha[rotatelow % 26]
		if char in ALPHA:
			rotatecap = position + rot
			return ALPHA[rotatecap % 26]
	else:
		return char
        
def encrypt(text, rot):
	rot = int(rot)
	encrypted = ""		
	for char in text:
		rotatechar = rotate_character(char, rot)
		encrypted += rotatechar
	return encrypted