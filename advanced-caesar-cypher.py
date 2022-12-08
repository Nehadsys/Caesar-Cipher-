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
        # We subtract 65 from the ASCII code to make 'A' the starting point,
        # then add the key and take the modulo 26 to handle the wrap around from 'Z' to 'A'
        # Finally, we add 65 to the result to shift it back to the correct ASCII range
        shifted_ASCII = ((((ASCII - 65) + Key) % 26) + ord("A"))
        # Convert the ASCII code to the corresponding character and add it to the encrypted text
        encrypted_text += chr(shifted_ASCII)
    # Check if the character is a lowercase letter
    elif char.islower():
        # Convert the character to ASCII code
        ASCII = ord(char)
        # Shift the ASCII code by the specified key
        # We subtract 97 from the ASCII code to make 'a' the starting point,
        # then add the key and take the modulo 26 to handle the wrap around from 'z' to 'a'
        # Finally, we add 97 to the result to shift it back to the correct ASCII range
        shifted_ASCII = ((((ASCII - 97) + Key) % 26) + ord("a"))
        # Convert the ASCII code to the corresponding character and add it to the encrypted text
        encrypted_text += chr(shifted_ASCII)
    # Check if the character is a space
    elif char == " ":
        # Add a space to the encrypted text
        encrypted_text += " "

# Print the encrypted text
print(encrypted_text, end='')
