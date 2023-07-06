text = input("Input the text you want to encrypt: ")

# The key used for encryption
Key = eval(input("Input a key to shift the letters: "))

# The resulting encrypted text will be stored in this variable
encrypted_text = ""

# Loop through each character in the original text
for char in text:
    # Check if the character is an uppercase letter
    if char.isupper():
        # Convert the character to ASCII code
        ASCII = ord(char)
        # Shift the ASCII code by the specified key
        shifted_ASCII = ((((ASCII - 65) + Key) % 26) + ord("A"))
        # Convert the ASCII code to the corresponding character and add it to the encrypted text
        encrypted_text += chr(shifted_ASCII)
    # Check if the character is a lowercase letter
    elif char.islower():
        # Convert the character to ASCII code
        ASCII = ord(char)
        # Shift the ASCII code by the specified key
        shifted_ASCII = ((((ASCII - 97) + Key) % 26) + ord("a"))
        # Convert the ASCII code to the corresponding character and add it to the encrypted text
        encrypted_text += chr(shifted_ASCII)
    # Check if the character is a space
    elif char == " ":
        # Add a space to the encrypted text
        encrypted_text += " "

# Print the encrypted text
print(encrypted_text, end='')
