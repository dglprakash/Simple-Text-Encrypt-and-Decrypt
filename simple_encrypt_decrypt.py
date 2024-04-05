from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import qrcode

def generate_iv_from_key(key):
    iv = hashlib.sha256(key).digest()[:16]
    return iv

def generate_fixed_key(private_pass):
    fixed_key = (private_pass * 256).encode()
    return fixed_key

def encrypt_text(plaintext, fixed_key):
    fixed_key_16 = fixed_key[:16]
    iv = generate_iv_from_key(fixed_key)
    cipher = AES.new(fixed_key_16, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return ciphertext

def decrypt_text(ciphertext, fixed_key):
    fixed_key_16 = fixed_key[:16]
    iv = generate_iv_from_key(fixed_key)
    cipher = AES.new(fixed_key_16, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text.decode()

def save_to_file(text, filename):
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print(f"Text saved to {filename}")
    except IOError:
        print(f"Error: Failed to save text to {filename}")

def create_qr_code(text, filename):
    try:
        qr = qrcode.make(text)
        qr.save(filename)
        print(f"QR code saved to {filename}")
    except IOError:
        print(f"Error: Failed to save QR code to {filename}")


def main():
    choice = input("Do you want to Encrypt or Decrypt: (e/d)? ")

    if choice.lower() == 'e':
        plaintext = input("Enter the text to Encrypt: ")
        private_pass = input("Enter your Private Password: ")
        fixed_key = generate_fixed_key(private_pass)
        ciphertext = encrypt_text(plaintext, fixed_key)
        print("Encrypted text:", ciphertext.hex())
        
        save_option = input("Do you want to Save the encrypted text file: (y/n) ")
        if save_option.lower() == 'y':
            filename = input("Enter the Filename: ")
            save_to_file(ciphertext.hex(), filename + '_encrypted.txt')
        
        qr_option = input("Do you want to create a QR code: (y/n) ")
        if qr_option.lower() == 'y':
            qr_filename = input("Enter the Filename: ")
            create_qr_code(ciphertext.hex(), qr_filename + '_encrypted.png')
            
    elif choice.lower() == 'd':
        try:
            ciphertext = bytes.fromhex(input("Enter the Encrypted text: "))
            private_pass = input("Enter your private password: ")
            fixed_key = generate_fixed_key(private_pass)
            decrypted_text = decrypt_text(ciphertext, fixed_key)
            print("Decrypted text:", decrypted_text)
            
            save_option = input("Do you want to Save the Decrypted text file: (y/n) ")
            if save_option.lower() == 'y':
                filename = input("Enter the Filename: ")
                save_to_file(decrypted_text, filename + '_decrypted.txt')
                
            qr_option = input("Do you want to create a QR code: (y/n) ")
            if qr_option.lower() == 'y':
                qr_filename = input("Enter the Filename: ")
                create_qr_code(decrypted_text, qr_filename + '_decrypted.png')
                
        except ValueError:
            print("Invalid hexadecimal format for ciphertext.")
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()