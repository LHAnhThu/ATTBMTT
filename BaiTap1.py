plaintext = "Le Hoang Anh Thu"
k = 17
ciphertext = ""

print("Ho va ten sinh vien:", plaintext)
print("So thu tu:", k)

for char in plaintext:
    if char.isupper():
        ciphertext += chr((ord(char) - ord('A') + k) % 26 + ord('A'))

    elif char.islower():
        ciphertext += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    
    else:
        ciphertext += char

print("Ho va ten ma hoa:", ciphertext)