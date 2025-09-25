plaintext = "Le Hoang Anh Thu"
k = 17  
ciphertext = ""

print("Ho va ten sinh vien:", plaintext)
print("So thu tu:", k)

for char in plaintext:
    if char.isupper(): 
        P = ord(char) - ord('A')
        C = (P + k) % 26
        ciphertext += chr(C + ord('A'))
    elif char.islower():
        P = ord(char) - ord('a')
        C = (P + k) % 26
        ciphertext += chr(C + ord('a'))
    else: 
        ciphertext += char

print("Ho va ten ma hoa:", ciphertext)
