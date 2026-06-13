from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)
with open("secret.txt", "rb") as original_file:
    original_data = original_file.read()

encrypted_data = fernet.encrypt(original_data)

with open("secret_encrypted.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")
print(f"Original data: {original_data}")
print(f"Encrypted data: {encrypted_data}")