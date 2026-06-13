from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n Key generated and saved to secret.key!\n")

def load_key():
    if not os.path.exists("secret.key"):
        print("\n No key found! Please generate a key first.\n")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file():
    key = load_key()
    if key is None:
        return
    filename = input("Enter the filename to encrypt (e.g. secret.txt): ")
    if not os.path.exists(filename):
        print(f"\n File '{filename}' not found!\n")
        return
    fernet = Fernet(key)
    with open(filename, "rb") as f:
        original_data = f.read()
    encrypted_data = fernet.encrypt(original_data)
    encrypted_filename = "encrypted_" + filename
    with open(encrypted_filename, "wb") as f:
        f.write(encrypted_data)
    print(f"\n File encrypted and saved as '{encrypted_filename}'!\n")

def decrypt_file():
    key = load_key()
    if key is None:
        return
    filename = input("Enter the filename to decrypt (e.g. encrypted_secret.txt): ")
    if not os.path.exists(filename):
        print(f"\n File '{filename}' not found!\n")
        return
    fernet = Fernet(key)
    with open(filename, "rb") as f:
        encrypted_data = f.read()
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        decrypted_filename = "decrypted_" + filename
        with open(decrypted_filename, "wb") as f:
            f.write(decrypted_data)
        print(f"\n File decrypted and saved as '{decrypted_filename}'!\n")
    except:
        print("\n Decryption failed! Wrong key or corrupted file.\n")

def menu():
    while True:
        print("==================================")
        print("         Python Crypto Tool       ")
        print("==================================")
        print("1. Generate Encryption Key")
        print("2. Encrypt a File")
        print("3. Decrypt a File")
        print("4. Exit")
        print("==================================")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            encrypt_file()
        elif choice == "3":
            decrypt_file()
        elif choice == "4":
            print("\nGoodbye! \n")
            break
        else:
            print("\n Invalid option. Please choose 1-4.\n")

menu()