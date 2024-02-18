try:
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input('Type encode to Encrypt or Type decode to Decrypt: ')
    text = input('Type Your Message: ').lower() # Enter a message you want to encript
    shift = int(input('Type Shift No: '))  # How many letter you want to shift the string
    def encrypt(plain_text,shift_no): # Encreption Function
        cipher_text = '' # define variable that contain an empty string
        for letter in plain_text: # Loop through the text the that the user enter  
            position = alphabet.index(letter) # find the index of the every letter in the list and assigned it to the position variable
            new_position = position + shift_no # Add the index of the every letter with the shift no that the user has enter and assigned it to the new_position variable
            new_letter = alphabet[new_position] # accessing letters in the alphabet list by the index value of new_position variable and assigned it to the new_letter variable
            cipher_text += new_letter # concatenating the cipher empty string with the letter of new_letter variable 
        print(f'The Encoded Text is: {cipher_text}') # printing message and cipher variable

except ValueError: # it is for the error if the user enter a space in the string.
    print('Space is not allowed in the string!')

#decryption
def decrypt(cipher_text,shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        new_letter=alphabet[new_position]
        plain_text+=new_letter
    print(f"the decrypted text is: {plain_text}")


if direction == 'encode':
    encrypt(plain_text=text,shift_no=shift) # Calling a function by passing the value of text and shift variable
elif direction == 'decode':
    decrypt(cipher_text=text,shift_amount=shift) # Calling a function by passing the value of text and shift variable
else:
    print('Invalid!')