from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)
with open("secret_encrypted.txt", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = fernet.decrypt(encrypted_data)
with open("secret_decrypted.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully!")
print(f"Encrypted message: {encrypted_data}")
print(f"Decrypted message: {decrypted_data}")